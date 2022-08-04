from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login,logout
from rest_framework import status

class LoginApi(APIView):
    def post(self,request,format=None):
        username=request.data.get('Username')
        password=request.data.get('Password')
        user=authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user=user)
                return Response({'Success':'Logged In'},status.HTTP_200_OK)
            return Response(status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status.HTTP_401_UNAUTHORIZED)