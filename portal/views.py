from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import FacultyTimetable

@login_required
def faculty_courses(request):
    today_day = datetime.now().strftime("%a")

    today_classes = FacultyTimetable.objects.filter(
        faculty=request.user,
        day=today_day
    )

    weekly_classes = FacultyTimetable.objects.filter(
        faculty=request.user
    ).order_by('day', 'start_time')

    return render(request, 'faculty_courses.html', {
        'today_classes': today_classes,
        'weekly_classes': weekly_classes,
    })
