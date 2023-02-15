from django.contrib import admin
from .models import Product, Color, Size, Information
# Register your models here.


class InformationAdmin(admin.StackedInline):
    model = Information


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    inlines = (InformationAdmin,)


admin.site.register(Size)
admin.site.register(Color)

