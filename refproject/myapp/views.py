from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import User
# Create your views here.


def guest(function):
    return HttpResponse('Guest Page')
def junk(request):
    return HttpResponse('Junk Page')
def add(request,a,b):
    return HttpResponse('Add page')
def sub(request):
    return HttpResponse('Sub page')
def calcmul(request):
    return HttpResponse('Calcmul page')

def home(request):
    return render(request,'home.html')
def adminlogin(request):
   return render(request,'adminlogin.html')
def userreg(request):
    return render(request,'userreg.html')
def userlogin(request):
    return render(request,'userlogin.html')
def contactus(request):
    return render(request,'contactus.html')


def checkadmin(request):
    if request.method=='POST':
        aid  = request.POST['aid']
        apwd = request.POST['apwd']
        if aid=='admin' and apwd=='admin':
            return render(request,'adminhome.html')
        else:
            return HttpResponse('InValid Login')

def userregistration(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() # saves all values to DB table
            #return redirect('userlogin.html')
            return render(request,'userlogin.html')
    else:
        form = RegistrationForm()
    return render(request,'userreg.html',{'form':form})


#adminhome.html views
def adminhome(request):
    return render(request,'adminhome.html')
def adminlogout(request):
    return render(request,'adminlogin.html')
def viewusers(request):
    users = User.objects.all() #~SELECT * FROM user_table
    return render(request,'viewusers.html',{'users':users})


#model->class
#Model Name -> User
#Column Names -> Id,Name,Gender,Location
#Using the User model a form with fields Id,Name,Gender,Location can be created