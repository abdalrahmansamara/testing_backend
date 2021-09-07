from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import SignupSerializer, UserSerializer

# Create your views here.

class SignUpView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    queryset=User.objects.all()

class GetUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
