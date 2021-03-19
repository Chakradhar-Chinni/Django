from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

def pfunction(request):
    return HttpResponse("p function")
def mainpagefunction(request):
    return render(request,"project.html")
def userpage(request):
    return redirect("user")