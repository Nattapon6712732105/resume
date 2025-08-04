from django.shortcuts import render
from httpx import request


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def forpage(request):
    contact = {}
    contact['count'] = list(range(1, 11))
    
    return render(request, 'for.html', context)