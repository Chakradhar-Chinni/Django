from django.shortcuts import render
from django.http import HttpResponse
def tuserfunction(request):
    return HttpResponse("tuser -> views.py ->tempapp")
def tuser1function(request):
    return HttpResponse("tuser1 -> views.py -> tempapp")
def tuser2function(request):
    return HttpResponse("tuser2 -> views.py -> tempapp")
def tuser3function(request):
    return HttpResponse("tuser3->views.py")    