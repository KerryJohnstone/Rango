from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = "Click here to view " + '<a href="/rango/about/">About</a> ' + "Rango says hey there partner!"
    return HttpResponse(html)

def about(request):
    html="Click to return to " + '<a href="/rango/">Main Page</a> ' + "Rango says here is the about page."
    return HttpResponse(html)

