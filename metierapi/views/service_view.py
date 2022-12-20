from rest_framework.decorators import action
from django.http import HttpResponseServerError
from django.db.models import Case, When, Value, IntegerField, BooleanField
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models import MetierUser, MetierCustomer
from metierapi.models.service import Service
from metierapi.models.reaction import Reaction
from metierapi.models.comment import Comment
from metierapi.models.service_reaction import ServiceReaction

class ServiceView(ViewSet):
    def retrieve(self, request, pk):
       
        service_view = Service.objects.get(pk=pk)
        
    
        serialized =ServiceSerializer(service_view, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
       
        service_view = Service.objects.all().order_by('publication_date')
 
        serialized = ServiceSerializer(service_view, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
       
        creator = MetierUser.objects.get(user=request.auth.user)

        service = Service.objects.create(
            creator=creator,
            service=request.data["service"],
            publication_date=request.data["publication_date"],
            image=request.data["image"],
            body=request.data["body"],
            price=request.data["price"]
        )
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def update(self, request, pk):
        

        service = Service.objects.get(pk=pk)
        service.service = request.data["service"]
        service.image = request.data["image"]
        service.body = request.data["body"]
        service.price = request.data["price"]
        reaction = ReactionsSerializer(request.data['reactions'])
        service.reactions.set(reaction)
        comment = Comment.objects.get(pk=request.data['comment'])
        service.comment = comment
        service.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)  

    def destroy(self, request, pk):
            service = Service.objects.get(pk=pk)
            service.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)

    # @action(methods=['post', 'delete'], detail=True)

    # def servicereaction(self, request, pk=None):

    #     service = Service.objects.get(pk=pk)
    #     if request.method == "POST":
    #         reaction = Reaction.objects.get(pk=request.data["reactionId"])
    #         service.reactions.add(reaction)
    #         return Response({"Reaction has been added"}, status=status.HTTP_204_NO_CONTENT)

    #     elif request.method == "DELETE":
    #         reaction = Reaction.objects.get(pk=request.data["reactionId"])
    #         service.reactions.delete(reaction)
    #         return Response({"Reaction has been removed"}, status=status.HTTP_204_NO_CONTENT)


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetierUser
        fields = ('id', 'full_name', )

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MetierUser
#         fields = ('id', 'customer', 'comment', 'created_on', )

class ReactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceReaction
        fields = ('id', 'reaction', 'customer', 'service',)

class ServiceSerializer(serializers.ModelSerializer):
    creator= CreatorSerializer(many=False)
    # comment = CommentSerializer(many=False)
    reactions = ReactionsSerializer(many=True)

    def create_or_update_reactions(self, reactions):
        reaction_ids = []
        for reaction in reactions:
            reactions_instance, created = ServiceReaction.objects.update_or_create(pk=reaction.get('id'), default=reaction)
            reaction_ids.append(reactions_instance.pk)
        return reaction_ids

    class Meta:
        model = Service
        fields = ('id', 'creator', 'is_creator',
        'service', 'publication_date', 'image', 'body', 
        'price', 'reactions', 'comment',)
        depth = 1
