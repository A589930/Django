from django.http import HttpResponse
from django.shortcuts import redirect, render
from courses.forms import RegisterForm , LoginForm
from django.views import View
from django.contrib.auth import logout
from django.views.generic.edit import FormView


class SignupView(FormView):
    template_name="courses/signup.html" 
    form_class = RegisterForm
    success_url  = '/login'
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
'''
class SignupView(View):
    def get(self, request):
        form=RegisterForm()
        return render(request,'courses/signup.html',{'form': form})
    def post(self, request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            if user is not None:
                return redirect('login')
        return render(request,'courses/signup.html',{'form': form})
'''                

class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'courses/login.html',{'form': form})
    
    def post(self,request):
        form = LoginForm(request,data=request.POST)
        context={
            "form": form,
        }
        if form.is_valid():
            return redirect('home')
        return render(request,'courses/login.html',context)
    
def signout(request):
    logout(request)
    return redirect('home')