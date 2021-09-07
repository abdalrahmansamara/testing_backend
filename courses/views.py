from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Courses
from .serializer import CoursesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsAdminUserOrReadOnly
# Create your views here.

class AllCourses(generics.ListCreateAPIView):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    permission_classes = (IsAdminUserOrReadOnly,)

class OneCourse(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    permission_classes = (IsAdminUserOrReadOnly,)