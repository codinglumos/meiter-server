"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models.favorite import Favorite


class FavoriteView(ViewSet):
     
    def list(self, request):
       
        favorites = Favorite.objects.all().order_by('service').values()
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
       
        favorite = Favorite.objects.get(pk=pk)
        serializer = FavoriteSerializer(favorite, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class FavoriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favorite
        fields = ('id', 'service', 'customer',)