from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Profile,Win,Comment,Like
from .serializer import RegistrationSerializer,LoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.
class RegistrationView(APIView):
    def get(self, request, format=None):
        users=User.objects.all()
        serializers = RegistrationSerializer(users, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():

            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token = Token.objects.create(user=user).key
            data['token'] = token

        else:
            data = serializer.errors
        return Response(data)

class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']

            user = authenticate(username=username, password=password)
            token, created = Token.objects.get_or_create(user=user)

            user_manager = Token.objects.get(key=token).user.manager
            if user_manager:
                user_role = 'Manager'
            else:
                user_role = 'Employee'

            data['token'] = token.key
            data['user_role'] = user_role

        else:
            data = serializer.errors

        return Response(data)
