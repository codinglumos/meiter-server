from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from metierapi.models.user import MetierUser
from django.db import IntegrityError
from rest_framework import status
from metierapi.models.metier_customer import MetierCustomer


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    
    username = request.data['username']
    password = request.data['password']
    authenticated_user = authenticate(username=username, password=password)
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            'staff': authenticated_user.is_staff,
            'id':authenticated_user.id,
            'first_name,':authenticated_user.first_name,
            'last_name,':authenticated_user.last_name
        }
        return Response(data)
    else:
            data = { 'valid': False }
            return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
   
    account_type = request.data.get('account_type', None)
    username = request.data.get('username', None)
    password = request.data.get('password', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    email = request.data.get('email', None)
    if account_type is not None \
        and username is not None \
        and password is not None \
        and first_name is not None \
        and last_name is not None \
        and email is not None:
        if account_type == 'customer':
            profile_image = request.data.get('profile_image', None)
            if profile_image is None:
                return Response(
                    {'message': 'You must provide an image for a customer'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        elif account_type == 'staff':
            bio = request.data.get('bio', None)
            profile_image = request.data.get('profile_image', None)

            if bio is None:
                return Response(
                    {'message': 'You must provide a bio for a creator'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            elif profile_image is None:
                return Response(
                    {'message': 'You must provide an image for a creator'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        else:
            return Response(
                {'message': 'Invalid account type. Valid values are \'customer\' or \'staff\''},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            new_user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email= request.data['email']
            )
        except IntegrityError:
            return Response(
                {'message': 'An account with that email address already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        account = None
        if account_type == 'customer':
            account = MetierCustomer.objects.create(
                profile_image=request.data['profile_image'],
                user=new_user
            )
        elif account_type == 'staff':
            new_user.is_staff = True
            new_user.save()
            account = MetierUser.objects.create(
                bio=request.data['bio'],
                profile_image=request.data['profile_image'],
                user=new_user
            )
        token = Token.objects.create(user=account.user)
        data = { 'token': token.key, 'staff': new_user.is_staff }
        return Response(data)
    return Response({'message': 'You must provide a username, password, first_name, last_name, email and account_type'}, status=status.HTTP_400_BAD_REQUEST)