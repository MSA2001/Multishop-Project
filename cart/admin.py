from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone', 'is_paid')
    inlines = (OrderItemAdmin,)
    list_filter = ('is_paid', 'created_at')
