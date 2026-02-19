from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()

    profile_image = models.ImageField(
        upload_to='profile_pics/',
        default='profile_pics/default.png'
    )

    def __str__(self):
        return self.user.username
