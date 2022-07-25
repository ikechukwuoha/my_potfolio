from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'ikechukwu/index.html')

def about(request):
    return render(request, 'ikechukwu/about.html')

def education(request):
    return render(request, 'ikechukwu/education.html')

def portfolio(request):
    return render(request, 'ikechukwu/portfolio.html')


def service(request):
    return render(request, 'ikechukwu/service.html')


def experience(request):
    return render(request, 'ikechukwu/experience.html')


def contact(request):
    return render(request, 'ikechukwu/contact.html')