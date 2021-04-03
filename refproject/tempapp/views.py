from django.shortcuts import render
from django.http import HttpResponse
from .forms import CandidateForm,ProductForm
from .models import Candidate,Product
# Create your views here.

def index(request):
    return render(request,'index.html')
    #return HttpResponse("From Temp app")
def login(request):
    return render(request,'login.html')
def managerlogout(request):
    return render(request,'login.html')
def checkmanager(request):
    if request.method=='POST':
        mid  = request.POST['mid']
        mpwd = request.POST['mpwd']
        if mid=='manager' and mpwd=='manager':
            #return HttpResponse("Valid Login")
            return render(request,'mgrlogin.html')
        else:
            return HttpResponse('Invalid Login')
def registeredusers(request):
    return render(request,'viewregusers.html')

def prolog(request):
    if request.method=='POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save() # saves data to table
            return HttpResponse("<h1>Data is inserted Successfully</h1>")
    else:
        form = CandidateForm()
    return render(request,'prolog.html',{'form':form})
def partnerlogistics(request):
    all_data = Candidate.objects.all()
    return render(request,'logisticpartners.html',{'data':all_data})