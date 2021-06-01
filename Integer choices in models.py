class Card(models.Model): 
  
    class Suit(models.IntegerChoices):       
        DIAMOND = 1    
        SPADE = 2      
        HEART = 3       
        CLUB = 4      
  
    suit = models.IntegerField(choices=Suit.choices)
     
    Source(official documentation): https://docs.djangoproject.com/en/dev/ref/models/fields/#integerfield   
 
        
   
    
 
 
