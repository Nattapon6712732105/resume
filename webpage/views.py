
from django.shortcuts import render
from . import models
from . import models

# เพิ่มฟังก์ชัน multiply ให้ตรงกับที่ urls.py เรียกใช้
def multiply(request):
    context = {}
    multiplier = None
    if request.method == 'POST' and request.POST.get('number'):
        try:
            multiplier = int(request.POST.get('number'))
        except (TypeError, ValueError):
            multiplier = None
    if multiplier and multiplier > 0:
        context['count'] = list(range(1, multiplier + 1))
        context['results'] = [(multiplier, i, multiplier * i) for i in context['count']]
    else:
        context['count'] = []
        context['results'] = []
    return render(request, 'multiply.html', context)
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def forpage(request):
    contact = {}
    contact['count'] = list(range(1, 11))

    return render(request, 'for.html', contact)

def students(request):
    context = {}
    context['title'] = "This is the students page."

    students = models.Students.objects.all()

    context['students'] = students
    return render(request, 'students.html', context)
