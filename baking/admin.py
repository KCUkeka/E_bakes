from django.contrib import admin
from .models import Bakery

# Register your models here.

class BakeryAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'quantity')
    
    
    
admin.site.register(Bakery, BakeryAdmin)