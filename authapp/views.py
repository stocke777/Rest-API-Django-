from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Profile
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
# Create your views here.

@api_view(['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def index(request):

    if request.method == "GET":
        # If the email is in database
        print(request.POST['email'])
        try:
            u = User.objects.get(email = request.POST['email'])
            data = {
                "id" : str(u.pk),
                "login_type" : "signin"
            }
            return Response(data = data, status = status.HTTP_200_OK)
        # If email is NOT in Database
        except:
            print("no user")
            data = {
                "id" : "not registered",
                "login_type" : "signUP"
            }
            return Response(data = data, status = status.HTTP_200_OK)
    elif request.method == "POST":

        # If we can get User and Password from request
        try:
            u = User.objects.get(id = request.POST['userId'])
            p = request.POST['password']
            currentpassword = u.password
            # If password is CORRECT
            if check_password(p, currentpassword):
                return Response(data = "LOGIN SUCCESS", status = status.HTTP_200_OK)
            # If password is WRONG
            else:
                return Response(data = "LOGIN FAILED", status = status.HTTP_200_OK)
        except:
            # If we can get email, pass, firstname, lastname from request
            try:
                email = request.POST['email']
                password = make_password(request.POST['password'])
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                user = User.objects.create(email = email, password = password)
                user.save()
                profile = Profile.objects.create(user = user, firstname = firstname, lastname = lastname)
                profile.save()
                return Response(data = "User Created", status = status.HTTP_200_OK)

            except:
                # If we get UserId 
                try:
                    uid = request.POST['userId']
                    # If we get UserId + favorite
                    try:
                        favorite = request.POST['favorite']
                        user = User.objects.get(id = uid)
                        profile = user.profile
                        l = list(str(user.profile.favorite).split(","))
                        print(l)
                        # If favorite is ALREADY in list
                        if favorite in l:
                            print("Its in the list")
                            l.remove(favorite)
                            profile.favorite = str(l)
                            profile.save()
                        # If new favorite item
                        else:
                            profile.favorite = str(user.profile.favorite) + favorite + ","
                            profile.save()
                            print(user.profile.favorite)
                        return Response(data = "favorite add/remove", status = status.HTTP_200_OK)  
                    # If only UserId was provided
                    except:
                        user = User.objects.get(id = uid)
                        data = {
                            'email':user.email,
                            'firstname':user.profile.firstname,
                            'lastname':user.profile.lastname,
                            'favorite':user.profile.favorite,
                        }
                        return Response(data = data, status = status.HTTP_200_OK)  
                except:
                    return Response(data = "Wrong", status = status.HTTP_200_OK)  

        
                              

