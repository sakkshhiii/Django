from django.shortcuts import render

from .models import Student




from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django is working 🚀")

from django.shortcuts import render, redirect
from .models import Student

# READ
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

# CREATE
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        Student.objects.create(name=name, email=email, age=age)
        return redirect('/')

    return render(request, 'add.html')

# DELETE
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')

# UPDATE
def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.save()
        return redirect('/')

    return render(request, 'add.html', {'student': student})