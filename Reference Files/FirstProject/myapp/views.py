from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import RegistrationForm
from .models import User

#from .models import UserModel

#def indexfunction(request):
#    return HttpResponse("My First Django Application from index function")
def userfunction(request):
    return HttpResponse("<h2>Django application from user page</h2>")
def guestfunction(request):
    return HttpResponse("<h1>Django application from guest page</h1>")
def userfunction1(request,id):
    return HttpResponse(id)
def guestfunction1(request,id):
    return HttpResponse(id)
def addfunction(request,a,b):
    return HttpResponse(a+b)
def subfunction(request,a,b):
    return HttpResponse(a-b)
def strfunction(request,name):
    return HttpResponse(name)
def calcmul(request):
    return HttpResponse(a*b)
def str1function(request,name,id):
    mydict ={
        "name" : name,
        "id" : id
    }
    return JsonResponse(mydict)
def appindexfunction(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contactus.html")
    #passing arguments to render function
def index(request):
    #return HttpResponse("Indexpage page")
    return render(request,"index.html",{"message":"Welcome to Home page Explore"})
def adminlogin(request):
    return render(request,"adminlogin.html",{"message":"Welcome Mr.Admin"})
def userlogin(request):
    return render(request,"userlogin.html",{"message":"Welcome dear user"})
def userreg(request):
    #return HttpResponse("Userreg page")
    return render(request,"userreg.html")
def contactpage(request):
    data ="This is contact page"
    return render(request,"contactus.html",{"message":data})
def checkadmin(request):
    if request.method=="POST":
        aid = request.POST['aid']
        apwd = request.POST['apwd'] 
        if aid=='admin' and apwd=='admin':
            #return render(request,"checkadmin.html")
            return HttpResponse("Valid Login")
        else:
            #return render(request,"checkadmin.html")
            return HttpResponse("InValid Login")

def userreg(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() #all values will be saved to user_table
    else:
        form = RegistrationForm()
    return render(request,'userreg.html',{'form':form})






    
