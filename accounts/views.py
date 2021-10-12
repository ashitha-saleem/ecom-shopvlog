from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def log(request,c_slug=None):
    if request.method=='POST':

        user_name = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credential')
            return redirect('lg')

    return render(request,'login.html')
def reg(request,c_slug=None):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name = request.POST['lname']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username taken')
                return redirect('rg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('rg')

            else:
                user=User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('created....')
                return redirect('/')

        else:
            messages.info(request, "pasword doesn't match")
            return redirect('rg')
    else:
        return render(request,'register.html')

def logout(request,c_slug=None):
    auth.logout(request)
    return redirect('/')

