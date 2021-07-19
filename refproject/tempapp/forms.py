from django import forms 
from .models import Candidate,Product
  
class CandidateForm(forms.ModelForm):  
    class Meta:  
        model = Candidate               
        fields = "__all__"      
             
class ProductForm(forms.ModelForm):    
    class Meta:   
        model = Product    
        fields = "__all__"     
  
 
