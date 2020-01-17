from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse('Hello')

def home(request):
    return render(request, 'home.html', {'hithere':'This is me'})

def form(request):
    return render(request, 'form.html')

def count(request):
    return render(request, 'count.html')

def eggs(request):
    return HttpResponse('<h1>Eggs are great !</h1>')
