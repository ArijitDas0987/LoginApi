from django.shortcuts import render
from .models import UserModel
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User

class Get_Create_User(ListCreateAPIView):
    queryset=UserModel.objects.all()
    serializer_class=UserSerializer
    

class Retrieve_Update_Delete_User(RetrieveUpdateDestroyAPIView):
    queryset=UserModel.objects.all()
    serializer_class=UserSerializer

