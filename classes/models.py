from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Course(models.Model):
    
    GRADE_CHOICES = [
        ("A+", "A+"),
        ("A", "A"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B", "B"),
        ("B-", "B-"),
        ("C+", "C+"),
        ("C", "C"),
        ("C-", "C-"),
        ("D+", "D+"),
        ("D", "D"),
        ("D-", "D-"),
        ("F", "F"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=15, blank=True)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    credits = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.code}: {self.name} - Grade: {self.grade} Credits: {self.credits}"


