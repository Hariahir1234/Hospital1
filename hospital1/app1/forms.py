from django import forms
from .models import hospital,patient,doctor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class newuserform(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username','email','password1','password2')
    

class patientnew(forms.ModelForm):
    class Meta:
        model = patient
        fields = '__all__'
        
class doctornew(forms.ModelForm):
    class Meta:
        model = doctor
        fields = '__all__'
        
class hospitalnew(forms.ModelForm):
    class Meta:
        model = hospital
        fields = '__all__'
        
         