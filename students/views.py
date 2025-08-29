from django.shortcuts import render, redirect, get_object_or_404
from .models import Student  # import your model

def student_list(request):
    students = Student.objects.all()  # fetch all students from DB
    return render(request, "student_list.html", {"students": students})
