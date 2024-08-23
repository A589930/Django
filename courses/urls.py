from courses.views import home, coursePage, SignupView, LoginView , signout, checkout, verify_payment,mycourses
from django.contrib import admin
from django.urls import path, include
from codewithvijay.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path("", home, name='home'),
    path("logout", signout, name='logout'),
    path("mycourses", mycourses, name='mycourses'),
    path("login", LoginView.as_view(), name='login'),
    path("signup", SignupView.as_view(), name='signup'),
    path("course/<str:slug>", coursePage, name='coursepage'),
    path("check-out/<str:slug>", checkout, name='checkout'),
    path("verify_payment", verify_payment, name='verify_payment'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)