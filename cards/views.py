from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import *

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render (request,'registration/signUp_form.html', {'form':form})  

@login_required(login_url='/accounts/login/')
def index(request):
    document = Document.all_documents()
    json_documents = []
    for document in document:
        picture = Profile.objects.filter(user=document.user.id).first()
        if picture:
            picture = picture.profile_pic.url
        else:
            picture = ''
        obj = dict(
            title = document.title,
            image = document.image,
            content = document.description,
            date_created = document.date_created,
            courses = document.user.username
        )   
        json_documents.append(obj) 
    return render(request, 'index.html', {"json_documents": json_documents})                   
