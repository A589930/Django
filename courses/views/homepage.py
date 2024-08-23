
from django.http import HttpResponse
from django.shortcuts import  render
from courses.models.course import Course

def home(request):
    courses = Course.objects.all()
    print(courses)
    return render(request, 'courses/home.html', {'courses':courses})
