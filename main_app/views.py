from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import UserInfo
from django.http import JsonResponse
import os
import uuid

def get_user_info_form(request):
	return render(request, 'main_app/get_user_info_form.html')

def save_user_info(request):
    # print(request.POST)
    uploadFolder = settings.UPLOAD_DIR
    hashValue = str(uuid.uuid4()) # create a unique hash (or id)   
    uploaded_file = request.FILES.get("profilePic")
    # print("Uploaded file:", uploaded_file)
    up = str(uploadFolder)
    filename_ = str(hashValue) + '_' + uploaded_file.name

    if uploaded_file:
        path = os.path.join(up, filename_)
        dest = open(path, '+wb')
        if uploaded_file.multiple_chunks():
            for chunk in uploaded_file.chunks():
                dest.write(chunk)
        else:
            dest.write(uploaded_file.read())
        dest.close()
    else:
        print("No File Found")

    # Store data in database
    userinfo = UserInfo()
    userinfo.firstname = request.POST.get('firstName')
    userinfo.lastname = request.POST.get('lastName')
    userinfo.email = request.POST.get('email')
    userinfo.phone_number = request.POST.get('phoneNumber')
    userinfo.address = request.POST.get('address')  
    userinfo.profile_picture_path = filename_
    userinfo.save()

    data = {
        'message': 'Success',
    }

    return JsonResponse(data, status=200)