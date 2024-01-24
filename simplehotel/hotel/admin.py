from django.contrib import admin

from .models import Reservation, Room, Booked

admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Booked)
