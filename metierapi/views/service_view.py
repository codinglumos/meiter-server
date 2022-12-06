from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models.service import Service
from metierapi.models.creator import Creator
from metierapi.models.comment import Comment

class ServiceView(ViewSet):

    def list(self, request):
     
        services = Service.objects.all()

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):

        service = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(service, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):

        creator = Creator.objects.get(user=request.auth.user)
        comment = Comment.objects.get(pk=request.data['comment'])

        service = Service.objects.create(
            image = request.data['image'],
            service = request.data['service'],
            body = request.data['body'],
            price = request.data['price'],
            creator = creator,
            comment = comment
        )
        serialized = ServiceSerializer(service, many=False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):

        service = Service.objects.get(pk=pk)
        service.service = request.data['service']
        service.image = request.data['image']
        service.body = request.data['body']
        service.price = request.data['price']
       
        service.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        service = Service.objects.get(pk=pk)
        service.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

# class CreatorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Creator
#         fields = ('id', 'full_name', 'bio', 'user', 'profile_image',)

class ServiceSerializer(serializers.ModelSerializer):
 
    #creator = CreatorSerializer(many=False)
    class Meta:
        model = Service
        fields = ('id', 'creator', 'service', 'image', 'body', 'price', 'comment',)
        #depth = 1