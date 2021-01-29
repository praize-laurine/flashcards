from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Images, Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['profile_pic', 'bio']    

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']    

class PostSubjectForm(forms.ModelForm):
    class Meta:
        model = Images
        exclude = ['user',]
 

