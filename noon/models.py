from django.db import models

class Web(models.Model):
    name = models.CharField(max_length=25)
    data = models.CharField(max_length=50)

def __str__(self):
        return self.Name



    

# Create your models here.
