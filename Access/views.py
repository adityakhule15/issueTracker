import hashlib
import json
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .models import Login, IssuList
from .serializers import LoginSerializer, IssuListSerializer 



@csrf_exempt
class IssusList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request,Email):
        login = Login.objects.filter(Email =Email)
        serializer=LoginSerializer(login,many=True)
        login_serializer1 = json.dumps(serializer.data)
        login_serializer = json.loads(login_serializer1)
        for data_ in login_serializer:
            if data_['Roles']=='Super Admin':
                prod=IssuList()
                prod.Email=Email
                prod.Tags=request.POST.get('Tags')
                prod.Body=request.POST.get('Body')
                prod.Heading=request.POST.get('Heading')
                prod.save()
                return HttpResponse("Added Successfully")
            
            elif data_['Roles']=='Manager':
                prod=IssuList()
                prod.Email=Email
                prod.Tags=request.POST.get('Tags')
                prod.Body=request.POST.get('Body')
                prod.Heading=request.POST.get('Heading')
                prod.save()
                return HttpResponse("Added Successfully")

            elif data_['Roles']=='QA':
                prod=IssuList()
                prod.Email=Email
                prod.Tags=request.POST.get('Tags')
                prod.Body=request.POST.get('Body')
                prod.Heading=request.POST.get('Heading')
                prod.save()
                return HttpResponse("Added Successfully")

        return HttpResponse("Don't Have access")

        
    @csrf_exempt
    def edit(request,Email,ID):
        login = Login.objects.filter(Email =Email)
        serializer=LoginSerializer(login,many=True)
        login_serializer1 = json.dumps(serializer.data)
        login_serializer = json.loads(login_serializer1)
        for data_ in login_serializer:
            if data_['Roles']=='Super Admin':
                IssuList.objects.filter(Id = ID).update(
                Tags=request.POST.get('Tags'),
                Body=request.POST.get('Body'),
                Heading=request.POST.get('Heading'),
                )
                return HttpResponse("Updated Successfully")
            
            elif data_['Roles']=='Manager':
                IssuList.objects.filter(Id = ID).update(
                Tags=request.POST.get('Tags'),
                Body=request.POST.get('Body'),
                Heading=request.POST.get('Heading'),
                )
                return HttpResponse("Updated Successfully")

        return HttpResponse("Don't Have access")

    @csrf_exempt
    def view(request):
                Issu1=IssuList.objects.all()
                serializer = IssuListSerializer(Issu1, many = True)
                total_Issu1 = json.dumps(serializer.data)
                total_Issu = json.loads(total_Issu1)
                return render(request, 'issuList.html', {'Issus':total_Issu})




    @csrf_exempt
    def delete(request,Email,ID):
        login = Login.objects.filter(Email =Email)
        serializer=LoginSerializer(login,many=True)
        login_serializer1 = json.dumps(serializer.data)
        login_serializer = json.loads(login_serializer1)
        for data_ in login_serializer:
            if data_['Roles']=='Super Admin':
                Issu1=IssuList.objects.filter(Id = ID).all()
                Issu1.delete()
                return HttpResponse("Deleted Successfully")                
        return HttpResponse("Don't Have access")
        

    @csrf_exempt
    def login(request):
            login = Login.objects.filter(Email = request.POST.get('Email'))
            serializer=LoginSerializer(login,many=True)
            login_serializer1 = json.dumps(serializer.data)
            login_serializer = json.loads(login_serializer1)
            for item in login_serializer:
                sha_salt = item['Salt']
                Encrypted_Password = hashlib.pbkdf2_hmac('sha256', request.POST.get('Password').encode('utf-8'), bytes(sha_salt, 'utf-8'), 100000)
                if item['Password'] == str(Encrypted_Password):
                    print("Success")
                    if item['Roles']=='Client':
                        return render(request,'home.html')
                    else:
                        return render(request,'issuList.html')

    
            return JsonResponse("Password Authentication Failed",safe=False)

    @csrf_exempt
    def add(request):
            frProd = Login()
            frProd.Name=request.POST.get('Name')
            frProd.Email=request.POST.get('Email')
            frProd.Roles=request.POST.get('Roles')
            sha_salt = os.urandom(32)
            frProd.Salt = sha_salt
            new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('Password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
            frProd.Password= new_key
            frProd.save()
            
            return JsonResponse("Added Successfully",safe=False)

