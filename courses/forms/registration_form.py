from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=20, required=True)
    last_name=forms.CharField(max_length=20, required=True)
    email=forms.EmailField(max_length=30,required=True)
    
    class Meta:
        model=User
        fields=["first_name","last_name","username","email",'password1','password2']

    def clean_email(self):
        email=self.cleaned_data.get('email')
        user=None
        try:
            user=User.objects.get(email=email)
        except:
            return email
        if user is not None:
            raise forms.ValidationError("User already exists")