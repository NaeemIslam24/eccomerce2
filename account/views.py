from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . models import *


# Create your views here.
def login_register(request):

    template = 'login.html'

    if request.method == 'POST':

        uname = request.POST.get('user')
        psd = request.POST.get('pass')


        user = authenticate(request, username=uname, password=psd)

        if user is not None:
            login(request, user)
            return redirect('index')
    
    if request.method == 'POST':

        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        c_password = request.POST.get('confirm_pass')

        if password == c_password:

            if User.objects.filter(username=uname).exists():

                print('user name exist')

            elif User.objects.filter(email=email).exists():

                print('email exist')

            else:
                user = User.objects.create_user(first_name = name,
                                                username = uname,
                                                email = email,
                                                password = password)

                user.save()          
                return redirect('login_register')

    return render(request, template_name=template)


def logoutuser(request):

    logout(request)

    return redirect('index')

def test(request):

    template = 'test.html'

    son = NorulIslam.objects.all()
    daughter = FiruzaIslam.objects.all()

    context = {
       'son': son,
       'daughter': daughter,
    }

    return render(request, template_name=template, context=context)