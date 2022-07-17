from django.contrib import admin
from .models import Event,Payments,Buyer,Seller

# Register your models here.
admin.site.register (Event)
admin.site.register (Payments)
admin.site.register (Buyer)
admin.site.register (Seller)