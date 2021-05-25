from django import forms
from .models import User
#from .models import modelnames  
   
class RegistrationForm(forms.ModelForm):  
    class Meta:      
        model = User   
        fields = "__all__" 
 
