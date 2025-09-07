
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Student
from .forms import StudentForm


# -------------------
# Authentication Views
# -------------------
def login_page(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_list')
        else:
            error = "Invalid username or password"
    return render(request, 'student_app/login.html', {'error': error})


def logout_page(request):
    logout(request)
    return redirect('login')


# -------------------
# CRUD Views
# -------------------
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_app/student_list.html', {'students': students})


@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_app/add_student.html', {'form': form})



@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)  # yaha form use karo
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_app/edit_student.html', {'form': form})


@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":   # confirm delete
        student.delete()   # ye sahi hai
        return redirect('student_list')
    return render(request, "student_app/delete_student.html", {"student": student})
