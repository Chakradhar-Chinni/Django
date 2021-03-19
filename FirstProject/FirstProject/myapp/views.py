from django.shortcuts import render
from django.http import HttpResponse
def indexfunction(request):
    return HttpResponse("My First Django Application from index function")
def userfunction(request):
    return HttpResponse("<h2>Django application from user function</h2>")
def user1function(request):
    return HttpResponse("<h1>Django application from user1 function</h1>")