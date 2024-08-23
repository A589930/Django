
from django.http import HttpResponse
from django.shortcuts import  redirect, render
from courses.models.course import Course
from courses.models.user_course import UserCourse
from courses.models.video import Video  
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def mycourses(request):
    user=request.user
    user_courses=UserCourse.objects.filter(user=user)
    context={
        'user_courses':user_courses
    }
    return render(request, 'courses/my_courses.html', context=context)

def coursePage(request, slug):
    print(request.user.is_authenticated)
    course  = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by('serial_number')
    if serial_number is None:
        serial_number = 1 
    print(serial_number, course)
    video=Video.objects.get(serial_number=serial_number, course=course)
    if video.is_preview == False:
        if request.user.is_authenticated == False:
            return redirect('login')
        else:
                try:
                    user_course = UserCourse.objects.get(user=request.user,course=course)
                except:
                    return redirect('checkout', slug=course.slug)
    context = {
        'course': course,
        'video': video,
        'videos': videos
    }
    return render(request, 'courses/course_page.html', context=context)
