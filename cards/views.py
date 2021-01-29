from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import *
from .models import Images
from rest_framework.response import Response
from django.contrib.auth.models import User




# Create your views here.
def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            # login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render (request,'registration/signUp_form.html', {'form':form})  


@login_required(login_url='/accounts/login/')
def index(request):
    image = Images.objects.all()
    print(image)
    return render(request, 'index.html', {'image' : image})    


def search_subject_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get('image')
        searched_images = Images.search_by_image_subject(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{"message":message, "image":searched_images})

    else:
        message = "You haven't searched for any  subject"  
        return render(request, 'search.html',{'message':message})


@login_required(login_url='/accounts/login/')
def userProfile(request):

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance = request.user)
        prof_form = UserProfileUpdateForm(request.POST,request.FILES, instance = request.user.profile)

        if user_form.is_valid and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            
            return redirect('index')

    else:
        user_form = UpdateUserForm(instance = request.user)
        prof_form = UserProfileUpdateForm(instance = request.user.profile)
    context = {
        'user_form': user_form,
        'prof_form': prof_form
    }     
    return render(request, 'userProfile.html', context) 


@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            prof_form.save()

            return redirect('index')

    else:
        user_form = UpdateUserForm(instance = request.user)
        prof_form = UserProfileUpdateForm(instance = request.user)

        context = {
            'user_form' : user_form,
            'prof_form' : prof_form
        }        

    return render(request, 'update_profile.html', context)    

@login_required(login_url='/accounts/login/')
def post_subject(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostSubjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
           
            image.save()
            
        return redirect('index')

    else:
        form = PostSubjectForm()
    return render(request, 'post_subject.html', {"form": form})

