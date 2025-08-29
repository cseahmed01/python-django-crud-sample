from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm  # import your form

def student_list(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students, "form": form})
