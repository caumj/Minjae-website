from django.contrib import admin
from .models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'purpose', 'period', 'schedule', 'email', 'is_complete')

admin.site.register(Order, OrderAdmin)
