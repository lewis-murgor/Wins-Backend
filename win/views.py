from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Profile,Win,Comment,Like
from .serializer import RegistrationSerializer,LoginSerializer,ProfileSerializer,WinSerializer,CommentSerializer
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

            data['token'] = token.key
            

        else:
            data = serializer.errors

        return Response(data)

class LogoutView(APIView):
    def get(self, request, format=None):
        tokens = Token.objects.filter(user=request.user)
        for token in tokens:
            token.delete()
        content = {'success': ('User logged out.')}
        return Response(content)

class ProfileView(APIView):
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializers = ProfileSerializer(profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class WinView(APIView):
    def get(self, request, format=None):
        wins = Win.objects.all()
        serializers = WinSerializer(wins, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = WinSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentView(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializers = CommentSerializer(comments, many=True)
        return Response(serializers.data)
