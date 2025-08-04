from django.urls import path
from .views import CourseCreateView, CourseListView, CourseDeleteView, CourseUpdateView

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("new/", CourseCreateView.as_view(), name="course_new"),
    path("<int:pk>/delete/", CourseDeleteView.as_view(), name="course_delete"),
    path("<int:pk>/edit/", CourseUpdateView.as_view(), name="course_edit")
]