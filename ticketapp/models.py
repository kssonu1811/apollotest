from django.db import models
from datetime import datetime


# Create your models here.
class Contact(models.Model):
    First_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=150)
    address = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.First_name

class status(models.Model):
    user = models.OneToOneField(Contact, on_delete=models.CASCADE,primary_key=True)
    choices = (
        ('process', 'process'),
        ('activate', 'activate'),
    )
    status = models.CharField(choices=choices, max_length=10)


    

