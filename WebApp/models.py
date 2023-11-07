from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=60)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

     #change the name of the object
    def __str__(self): 
        return self.name