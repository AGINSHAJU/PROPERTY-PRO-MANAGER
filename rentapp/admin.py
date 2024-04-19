from django.contrib import admin
from .models import booking, car, payments, room
# Register your models here.
admin.site.register(car)
admin.site.register(booking)
admin.site.register(payments)
admin.site.register(room)