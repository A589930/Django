from django.db import models
from courses.models import Course

class Video(models.Model):
    title=models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_preview=models.BooleanField(default=False)
    video_id=models.CharField(max_length=100, null=False)
    serial_number = models.IntegerField(null=False)

    def __str__(self):
        return self.title