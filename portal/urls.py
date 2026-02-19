from django.urls import path
from . import views

urlpatterns = [
    path('faculty/courses/', views.faculty_courses, name='faculty_courses'),
]
