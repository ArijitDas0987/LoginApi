from pickle import TRUE
from django import dispatch
from django.http import JsonResponse
from django.shortcuts import render
from requests import delete
from urllib3 import HTTPResponse
from .serializers import StudentSerialializer
from django.views import View
import io
from rest_framework.parsers import JSONParser
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.shortcuts import render

def show(request):
    return render(request,'template/index.html')

@method_decorator(csrf_exempt, name='dispatch')
class Studentview(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream_data=io.BytesIO(json_data)
        parse_data=JSONParser().parse(stream_data)
        id=parse_data.get('id',None)

        if id is not None:
            stu=Student.objects.get(id=id)
            converting_json_data=StudentSerialializer(stu)
            return JsonResponse(converting_json_data.data,safe=False)
        
        stu=Student.objects.all()
        converting_json_data=StudentSerialializer(stu,many=True)
        return JsonResponse(converting_json_data.data,safe=False)

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream_data=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream_data)
        serializer=StudentSerialializer(data=python_data)
        
        if serializer.is_valid():
            # User.objects.create_user('john', email='lennon@thebeatles.com', password='johnpassword', is_staff=True)
            serializer.save()
            text={'msg':"*** Data Created Successfully !! ***"}
            return JsonResponse(text, safe=False)
        return JsonResponse(serializer.errors,safe=False)

    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream_data=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream_data)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerialializer(stu,data=python_data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            text={'msg':'*** Data Updated Successfully !! ***'}
            return JsonResponse(text,safe=False)
        return JsonResponse(serializer.errors,safe=False)
           
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream_data=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream_data)
        id=python_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            stu.delete()
            text={'msg':'*** Data Deleted Successfully !! ***'}
            return JsonResponse(text,safe=False)
        stu=Student.objects.all()
        stu.delete()
        text={'msg':'*** Data Deleted Successfully !! ***'}
        return JsonResponse(text,safe=False)
    
