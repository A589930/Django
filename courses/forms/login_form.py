from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate , login 
from django.forms import ValidationError

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email Address",required=True, max_length=30)
    
    def clean(self):
        email=self.cleaned_data["username"]
        password=self.cleaned_data["password"]
        user=None
        try:
            user=User.objects.get(email=email)
            result=authenticate(username=user.username,password=password)
            if result is not None:
                login(self.request,result)
                return result
            else:
                raise ValidationError("Password is incorrect")
        except:
            raise ValidationError("User does not exist")