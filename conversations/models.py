from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampedModel):
    
    participants = models.ManyToManyField("users.User", blank=True)
    
    def __str__(self):
        return self.created

# Create your models here.
