from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models.creator import Creator

class CreatorView(ViewSet):

    def list(self, request):
    
        creators = Creator.objects.all()

        serializer = CreatorSerializer(creators, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
     
        creator = Creator.objects.get(pk=pk)
        serializer = CreatorSerializer(creator, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        creator = Creator.objects.get(pk=pk)
        creator.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('id', 'full_name', 'bio', 'user', 'profile_image',)
        depth = 1