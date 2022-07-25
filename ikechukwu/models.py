from email.policy import default
from django.db import models

# Create your models here.

class Iyke(models.Model):
    name = models.CharField(max_length=150, null=True)
    projects = models.CharField(max_length=150, null=True)
    pro_img = models.ImageField(upload_to= 'images',default='blank')
    
    
    def __str__(self):
        return self.name