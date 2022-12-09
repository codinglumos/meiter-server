from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models import MetierCustomer
from django.contrib.auth.models import User

class MetierCustomerView(ViewSet):
    def list(self, request):
       
        users = MetierCustomer.objects.all()
        serialized = MetierCustomerSerializer(users, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
   
    def retrieve(self, request, pk=None):
       
        user = MetierCustomer.objects.get(pk=pk)
        serialized = MetierCustomerSerializer(user, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

class MetierCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetierCustomer
        fields = ('id', 'full_name', 'profile_image', 'user',)