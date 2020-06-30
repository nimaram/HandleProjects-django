from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from .forms import UserRegisteration , UserLoginForm
from .models import User
def view_login(request):
    if request.user.is_authenticated:
        return redirect('project:home')
    else:
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,email=cd['email'],password=cd['password'])
                if user is not None:
                    login(request,user)
                    return redirect('project:home')    
        else:
            form = UserLoginForm()
        return render(request,'site/users/login.html',{'form':form})    
def view_register(request):
    if request.user.is_authenticated:
        return redirect('project:home')

    else:
        if request.method == 'POST':
            form = UserRegisteration(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = User.objects.create_user(cd['email'],cd['talents'],cd['password'])
                user.save()
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user2 = authenticate(email=email,password=password)
                login(request,user2)
                return redirect('project:home')
        else:
            form = UserRegisteration()
        return render(request,'site/users/sign-in.html',{'form':form})        


def view_logout(request):
    logout(request)
    return redirect('project:home')
