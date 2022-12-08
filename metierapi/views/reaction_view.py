from rest_framework.decorators import action
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models import Reaction

class ReactionsView(ViewSet):
    def list(self, request):
      
        reactions = Reaction.objects.all()
        serializer = ReactionSerializer(reactions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
       
        reaction = Reaction.objects.get(pk=pk)
        serializer = ReactionSerializer(reaction)
        return Response(serializer.data)

    def create(self, request):
       
        reaction = Reaction.objects.create(
            reaction=request.data["reaction"]
        )
        serializer = ReactionSerializer(reaction)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
      
        reaction = Reaction.objects.get(pk=pk)
        reaction.reaction = request.data["reaction"]
        reaction.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
      
        reaction = Reaction.objects.get(pk=pk)
        reaction.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ReactionSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Reaction
        fields = ('id', 'reaction')