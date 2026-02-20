from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import FacultyTimetable


@login_required
def faculty_courses(request):
    today_day = timezone.now().strftime("%A")

    today_classes = FacultyTimetable.objects.filter(
        faculty=request.user,
        day=today_day
    ).order_by('start_time')

    weekly_classes = FacultyTimetable.objects.filter(
        faculty=request.user
    ).order_by('day', 'start_time')

    return render(request, 'faculty_courses.html', {
        'today_classes': today_classes,
        'weekly_classes': weekly_classes,
        'today_day': today_day,
    })
