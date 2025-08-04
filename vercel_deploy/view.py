from django.shortcuts import render
from httpx import request


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def multiply(request):
    context = {}
    # context['count'] = list(range(1, 11))  # Example context variable
    context['message'] = "This is the for page."
    # multiplier = 2
    if request.method == 'POST' and request.POST.get('number') != '':
        multiplier = int(request.POST.get('number'))
        print(request.POST['number'])
        context['count'] = list(range(1, multiplier + 1))
    else:
        multiplier = 2
        number = 1
        context['count'] = list(range(1, 2))

    context['results'] = [(multiplier, i, multiplier * i) for i in context['count']]

    return render(request, 'multiply.html', context)