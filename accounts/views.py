from django.contrib import messages, auth
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from contacts.models import Contact


def register(request):

    if request.method=='POST':
        print('in post')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if (password==password2):
           if User.objects.filter(username=username).exists():
               print('one')
               messages.info(request,'username already taken')
               return redirect('register')
           elif User.objects.filter(email=email).exists():
               print('email already taken')
           else:
              print('ok')
              user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
              print(user.first_name)
              # user.save()
              messages.info(request,'user sucessfully created')
              login(request,user)
              return redirect('login')
        else:
            print('user not created')
            messages.error(request, 'user not created')
        return redirect('register')

    else:

        return render(request, 'register.html')

    # return render(request , 'register.html')

def login_(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user =auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'invalid password or username')
            return redirect('login')
    else:
        return render(request , 'login.html')


def dash(request):

    user_contact = Contact.objects.order_by('-Contact_date').filter(user_id=request.user.id)
    context = {
        'contact':user_contact
    }
    return render(request, 'dashboard.html', context)

def logout_(request):
    # return render(request, 'logout.html')
    logout(request)
    return redirect('index')