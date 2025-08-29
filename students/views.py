from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
 

def student_list(request):
    return render(request, "student_list.html")

