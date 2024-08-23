from django.db import models
from courses.models.user_course import UserCourse
from django.contrib.auth.models import User
from courses.models.course import Course

class Payment(models.Model):
    order_id = models.CharField(max_length=50,null=False)
    payment_id= models.CharField(max_length=50)
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE , blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status  = models.BooleanField(default=False)
        
    def __str__(self):
        return f'{self.order_id} - {self.payment_id} - {self.user_course}'