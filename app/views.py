from contextlib import _RedirectStream
from random import randint
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")


def SignupPage(request):
    return render(request,"app/signup.html")

#user registration
def RegisterUser(request):
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)
        if user:
            message="User already Exist"
            return render(request,"app/login.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(1000,9999)
                newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                newcand = Candidate.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
            else:
                message="Password doesn't match"
                return render(request,"app/signup.html",{'msg':message})
    elif request.POST['role']=="Company":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)
        if user:
            message="User already Exist"
            return render(request,"app/login.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(1000,9999)
                newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                newcomp = Company.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})


def OTPPage(request):
    return render(request,"app/otpverify.html")


def OTPVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)
    if user:
        if user.otp == otp:
            return render(request,"app/login.html",{'msg':"OTP verify succuessfully", 'email': email})
        else:
            return render(request,"app/otpverify.html",{'msg':"OTP is incorrect", 'email': email})
    else:
        return render(request,"app/signup.html")


def LoginPage(request):
    return render(request,"app/login.html")


def UserLogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        #Checking the emailid with database
        user = UserMaster.objects.get(email=email)

        if user:
            if user.password ==  password and user.role=="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['contact'] = can.contact
                request.session['email'] = user.email
                request.session['role'] = user.role
                return render(request, "app/index.html")

            elif user.password ==  password and user.role=="Company":
                com = Company.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['firstname'] = com.firstname
                request.session['lastname'] = com.lastname
                request.session['contact'] = com.contact
                request.session['email'] = user.email
                request.session['role'] = user.role
                return render(request, "app/index.html")

            else:
                message= "Password Doesn't match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message="User Doesn't Exist"
            return render(request,"app/register.html",{'msg':message})


def ProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    return render(request, "app/profile.html",{'user':user,'can':can})


def UpdateProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if request.method == "POST":
        if user.role == "Candidate":
            can = Candidate.objects.get(user_id=user)
            can.firstname = request.POST.get('firstname', can.firstname)
            can.lastname = request.POST.get('lastname', can.lastname)
            can.dob = request.POST.get('dob', can.dob)
            can.address = request.POST.get('address', can.address)
            can.state = request.POST.get('state', can.state)
            can.city = request.POST.get('city', can.city)
            can.highest_education = request.POST.get('education', can.highest_education)
            can.experience = request.POST.get('experience', can.experience)
            can.website = request.POST.get('website', can.website)
            can.description = request.POST.get('description', can.description)
            can.current_salary = request.POST.get('current-salary', can.current_salary)
            can.expected_salary = request.POST.get('expected-salary', can.expected_salary)
            can.gender = request.POST.get('gender', can.gender)
            if 'image' in request.FILES:
                can.profile_pic = request.FILES['image']
            can.contact = request.POST.get('contact', can.contact)
            can.save()
            return redirect('profile', pk=pk)
    return redirect('profile', pk=pk) 

def Logout(request):
    # Clear all session data
    request.session.flush()  # This is better than deleting individual keys
    return redirect('index')  # Redirect to a new URL.