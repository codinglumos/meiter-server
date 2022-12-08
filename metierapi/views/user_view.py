from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from metierapi.models import MetierUser
from django.contrib.auth.models import User

class MetierUserView(ViewSet):
    def retrieve(self, request, pk):
      
        user_view = MetierUser.objects.get(pk=pk)
        serialized = MetierUserSerializer(user_view, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    # View all User
    def list(self, request):
      
        user_view = MetierUser.objects.all()
        serialized = MetierUserSerializer(user_view, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        user = MetierUser.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class MetierUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetierUser
        fields = ('id', 'full_name','bio','profile_image', 'user',)
        # depth=1
