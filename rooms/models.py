from django.db import models
from core import models as core_models

# Create your models here.

class Room(core_models.TimeStampedModel):
    
    """ Room Model Definition """
    
    
    
    
    name = models.CharField(max_length=140)
    description = models.TextField()
    #country = 
    
    pass