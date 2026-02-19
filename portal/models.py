from django.db import models
from django.contrib.auth.models import User


class FacultyTimetable(models.Model):
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.subject} - {self.day} ({self.time})"
