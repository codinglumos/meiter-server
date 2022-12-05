"""View module for handling requests about creators"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models.creator import Creator



class CreatorView(ViewSet):
    """Metier creator view"""

    def list(self, request):
        """Handle GET requests to get all creators

        Returns:
            Response -- JSON serialized list of creators
        """
        creators = Creator.objects.all()

        serializer = CreatorSerializer(creators, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single creator

        Returns:
            Response -- JSON serialized creator
        """
        creator = Creator.objects.get(pk=pk)
        serializer = CreatorSerializer(creator, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class CreatorSerializer(serializers.ModelSerializer):
    """JSON serializer for creators"""
    class Meta:
        model = Creator
        fields = ('id', 'full_name', 'bio', 'user', 'profile_image',)
        depth = 1