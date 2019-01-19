from django.contrib import admin
from .models import product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','nameproduct','price','detail')

admin.site.register(product, ProductAdmin)

