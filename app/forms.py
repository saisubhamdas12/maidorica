from django import forms
from .models import *



class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        help_texts={'username':''}
class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['mobile','address','profile_pic','document']



#for teacher related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        help_texts={'username':''}
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['mobile','address','profile_pic']