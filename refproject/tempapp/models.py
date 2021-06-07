from django.db import models

# Create your models here.
class Candidate(models.Model):
    Product   = models.CharField(max_length=100,blank=False) 
    Logistics = models.CharField(max_length=100,blank=False)  
    class Meta: 
        db_table = "candidate_table"  
         
class Product(models.Model): 
    brand = models.CharField(max_length=100,blank=False) 
    origin = models.CharField(max_length=100,blank=False)
    class Meta:
        db_table = "product_table" 
 
