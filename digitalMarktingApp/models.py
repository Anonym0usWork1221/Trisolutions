from pyexpat import model
from django.db import models
from more_itertools import first

# Create your 

class ContactUS(models.Model):
    
    first_name = models.CharField(max_length=122)
    sur_name = models.CharField(max_length=122)
    email = models.EmailField()
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.first_name + " " + self.sur_name
