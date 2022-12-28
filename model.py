from django.db import models

class   contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    decs=models.TextField(max_length=122)
    Date=models.DateField(max_length=122)
   