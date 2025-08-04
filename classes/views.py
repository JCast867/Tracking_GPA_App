from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Course

# Create your views here.

GRADE_TO_GPA = {
    "A+": 4.33,
    "A": 4.00,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.00,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.00,
    "C-": 1.67,
    "D+": 1.33,
    "D": 1.00,
    "D-": 0.67,
    "F": 0
    }

class CourseCreateView(CreateView):
    model = Course
    template_name = "course_new.html"
    fields = ("name", "code", "grade", "credits")
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CourseListView(ListView):
    model = Course
    template_name = "gpa_list.html"
    context_object_name = "courses"
    
    def get_queryset(self):
        return Course.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        courses = context['courses']
        total_points  = 0
        total_credits = 0

        for course in courses:
            grade_value = GRADE_TO_GPA[course.grade]
            course_points = grade_value * course.credits
            total_points += course_points
            total_credits += course.credits

        if total_credits > 0:
            context['gpa'] = round(total_points / total_credits, 2)
        else:
            context['gpa'] = 0.00

        return context

