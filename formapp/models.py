from django.db import models

# Create your models here.



class Form(models.Model):

    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    message = models.CharField(max_length=200)