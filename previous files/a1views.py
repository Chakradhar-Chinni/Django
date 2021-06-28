from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def home(request):
    return HttpResponse("Hello World!! Welcome to Django!!"); 

return render(request, 'home.html')
  
    return render(request, 'home.html',{'name':'Chakradhar Chinni'})  
                                            
    ##name on the above line dynamically gives the value to home.html which is as {{name}}

    #edit: gitbash
