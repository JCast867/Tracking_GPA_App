from django.urls import path
from .views import CourseCreateView, CourseListView

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("new/", CourseCreateView.as_view(), name="course_new")
]