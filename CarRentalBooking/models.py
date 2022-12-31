from django.db import models
from datetime import datetime

class client(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Age = models.BinaryField()
    CellNo = models.BinaryField()
    Email = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)
    PetName = models.CharField(max_length=25)

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=25)
    subject = models.TextField(max_length=50)
    message = models.CharField(max_length=255)

class fleetmaster(models.Model):
    fleetnumber = models.CharField(max_length=10)
    fleetname = models.CharField(max_length=50)
    fleetbrand = models.CharField(max_length=50)
    enginecapacity = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    fleetmodel = models.CharField(max_length=50)
    fleetimg = models.CharField(max_length=50)
    fleetcategory = models.CharField(max_length=50)

class bookings(models.Model):
    fleetmasterid = models.ForeignKey(fleetmaster, on_delete=models.CASCADE)
    clientid = models.ForeignKey(client, on_delete=models.CASCADE)
    bookingdate = models.DateTimeField(default=datetime.now,blank=True)
    status = models.CharField(max_length=50)

class testimonials(models.Model):
    clientid = models.ForeignKey(client, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=255)