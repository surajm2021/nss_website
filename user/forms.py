from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from student.models import Profile
from .models import Document


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']
    def get_username(self):
        return forms.get_username


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
        