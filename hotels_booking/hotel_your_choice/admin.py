# hotel_your_choice/admin.py

from django.contrib import admin
from .models import Hotel, Booking

admin.site.register(Hotel)
admin.site.register(Booking)
