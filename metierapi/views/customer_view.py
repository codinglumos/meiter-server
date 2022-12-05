"""View module for handling requests about customers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models.customer import Customer



class CustomerView(ViewSet):
    """Metier customer view"""

    def list(self, request):
        """Handle GET requests to get all customers

        Returns:
            Response -- JSON serialized list of customers
        """
        customers = Customer.objects.all()

        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single customer

        Returns:
            Response -- JSON serialized customer
        """
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for customers"""
    class Meta:
        model = Customer
        fields = ('id', 'full_name', 'address', 'user',)
        depth = 1