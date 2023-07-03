from django.contrib import admin

# Register your models here.
from django.contrib.admin.decorators import register

from .models import *
admin.site.register(Profile)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Crop)
admin.site.register(Negotiation)
admin.site.register(Order)



