from django.shortcuts import render
from django.http import Http404
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

class SingleProfile(APIView):
    def get_profile(self, id):
        try:
            return Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        profile = self.get_profile(id)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, id, format=None):
        profile = self.get_profile(id)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id,format=None):
        profile = self.get_profile(id)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

class SingleWin(APIView):
    def get_win(self, id):
        try:
            return Win.objects.get(id=id)
        except Win.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        win = self.get_win(id)
        serializers = WinSerializer(win)
        return Response(serializers.data)

    def put(self, request, id, format=None):
        win = self.get_win(id)
        serializers = WinSerializer(win, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id,format=None):
        win = self.get_win(id)
        win.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentView(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializers = CommentSerializer(comments, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleComment(APIView):
    def get_comment(self, id):
        try:
            return Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        comment = self.get_comment(id=id)
        serializers = CommentSerializer(comment)
        return Response(serializers.data)

    def put(self, request, id, format=None):
        comment = self.get_comment(id)
        serializers = CommentSerializer(comment, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id,format=None):
        comment = self.get_comment(id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
