from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Profile,Win,Comment,Like
from .serializer import RegistrationSerializer

# Create your views here.
class RegistrationView(APIView):
    def get(self, request, format=None):
        users=User.objects.all()
        serializers = RegistrationSerializer(users, many=True)
        return Response(serializers.data)
