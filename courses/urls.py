from django.urls import path, include
from .views import AllCourses, OneCourse

urlpatterns = [
    path("", AllCourses.as_view(), name="all"),
    path("<int:pk>", OneCourse.as_view(), name="One"),
    ]
