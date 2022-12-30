from django.db import models

class client(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Age = models.BinaryField()
    CellNo = models.BinaryField()
    Email = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)
    PetName = models.CharField(max_length=25)
    Address = models.TextField()



# class contact(models.Model):
#     name = models.CharField(max_length=122)
#     email = models.CharField(max_length=122)
#     phone = models.CharField(max_length=12)
#     decs = models.TextField(max_length=122)
#     Date = models.DateField(max_length=122)
   