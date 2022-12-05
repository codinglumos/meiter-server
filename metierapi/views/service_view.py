"""View module for handling requests about services"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models.service import Service



class ServiceView(ViewSet):
    """Metier service view"""

    def list(self, request):
        """Handle GET requests to get all services

        Returns:
            Response -- JSON serialized list of services
        """
        services = Service.objects.all()

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single service

        Returns:
            Response -- JSON serialized service
        """
        service = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(service, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class ServiceSerializer(serializers.ModelSerializer):
    """JSON serializer for services"""
    class Meta:
        model = Service
        fields = ('id', 'creator', 'service', 'image', 'body', 'price', 'comment',)
        depth = 1