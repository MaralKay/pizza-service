from django.contrib import admin
from .models import Customer, Pizza, Order


admin.site.register(Customer)
admin.site.register(Pizza)
admin.site.register(Order)
