from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login.html')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        uname = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpass']
        if password==cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already Taken..!")
                # return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"You've already registered with this email")
                # return redirect('/')
            else:
                user=User.objects.create_user(username=uname,password=password,first_name=fname,last_name=lname,email=email)
                user.save()
                print("User created")
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
