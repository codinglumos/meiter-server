from rest_framework.decorators import action
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models import Comment, Service, MetierUser
from django.contrib.auth.models import User

class CommentView(ViewSet):
    def create(self, request, pk):
       
        service = Service.objects.get(pk=pk)
        customer = User.objects.get(user=request.auth.user)
        comment = Comment.objects.create(
            service=service,
            customer=customer,
            comment=request.data["comment"],
            created_on=request.data["created_on"]
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def destroy(self, request, pk):

        customer = User.objects.get(user=request.auth.user)
        comment = Comment.objects.get(pk=pk, customer=customer)
        comment.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
       
        if "service" in request.query_params:
            comments = Comment.objects.filter(service__id=request.query_params['service'])

        else:
            comments = Comment.objects.all()

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
       
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def update(self, request, pk=None):
       
        customer = User.objects.get(user=request.auth.user)
        service = Service.objects.get(pk=request.data["service"])
        comment = Comment.objects.get(pk=pk, customer=customer, service=service)
        comment.comment = request.data["comment"]
        comment.created_on = request.data["created_on"]
        comment.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT) 

class CommentSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Comment
        fields = ('id', 'customer', 'comment', 'created_on')
        depth = 1
