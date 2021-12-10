from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Product



class ProductAdmin(admin.ModelAdmin):
  fields = ('name','price','descrption','date_entry','photo')
  list_filter = (
    ('date_entry', DateFieldListFilter),
  )
  list_display = ('code','name','price','description','date_entry')

admin.site.register(Product,ProductAdmin)

