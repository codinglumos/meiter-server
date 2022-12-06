from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models.customer import Customer

class CustomerView(ViewSet):

    def list(self, request):

        customers = Customer.objects.all()

        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
    
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CustomerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Customer
        fields = ('id', 'full_name', 'address', 'user',)
        depth = 1