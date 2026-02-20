from django.db import models
from django.contrib.auth.models import User


class FacultyTimetable(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    faculty = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject} - {self.day}"
