from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,'Home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

