from django.contrib import admin
from CarRentalBooking.models import client, contact, fleetmaster

# Register your models here.
admin.site.register(client)
admin.site.register(contact)
admin.site.register(fleetmaster)