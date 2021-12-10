from django import forms
from users.models import Profile

from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.db.utils import IntegrityError
# Create your views here.
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import ProfileForm, SignupForm


def update_profile(request):
    profile=request.user.profile
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES) #LOS ARCHIVOS VIENEN DE UN ARCHIVO DE files
        if form.is_valid():
            data=form.cleaned_data
            profile.website=data['website']
            profile.phone_number=data['phone_number']
            profile.biography = data['biography']
            profile.picture=data['picture']
            profile.save()
            return redirect('login')
    else:
        form=ProfileForm()       

    return render(request=request,template_name='users/update_profile.html',context={'profile':Profile,'user':request.user,'form':form})

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'invalid username and password'})
    return render(request,'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    """Sign up view."""
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=SignupForm()
    return render(request=request,template_name='users/signup.html',
        context={'form':form}
    )

