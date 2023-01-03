from django.urls import reverse
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

     if "myServices" in request.query_params:
      user = MetierUser.objects.get(user=request.auth.user)
      service_view = Service.objects.all().order_by('publication_date').filter(creator=user)
     else:
      service_view = Service.objects.all().order_by('publication_date')


     serialized = ServiceSerializer(service_view, many=True, context={'request': request})
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
        # service.reactions.set = request.data['reactions']
        # comment = Comment.objects.get(pk=request.data['comment'])
        # service.comment = comment
        service.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)  

    def destroy(self, request, pk):
            service = Service.objects.get(pk=pk)
            service.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetierUser
        fields = ('id', 'full_name','bio','profile_image', 'user',)
        depth = 1

class ReactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceReaction
        fields = ('id', 'reaction', 'customer', 'service',)

class ServiceSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer()
    reactions = ReactionsSerializer(many=True)
    # delete_url = serializers.SerializerMethodField()
    # edit_url = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ('id', 'creator', 'service', 'publication_date', 'image', 'body', 'price', 'reactions',)
        depth = 2

    # def get_delete_url(self, obj):
    #     request = self.context.get('request')
    #     authenticated_username = request.auth.user.username
    #     service_creator_username = obj.creator.user.username
    #     if authenticated_username == service_creator_username:
    #         return reverse('service-delete', kwargs={'pk': obj.pk})
    #     return ''

    # def get_edit_url(self, obj):
    #      request = self.context.get('request')
    #      if obj.creator == request.user:
    #         return reverse("service-update", kwargs={"pk": obj.pk})
    #      return ''

