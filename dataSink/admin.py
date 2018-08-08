from django.contrib import admin
from .models import productForm, customerRegistration, dispatchOrder


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['product_category', 'product_class', 'product_code']
    search_fields = ['product_category', 'product_class', 'product_code']


class CustomerAdmin(admin.ModelAdmin):
    list_filter = ['cust_name', 'cust_city', 'customer_type', 'customer_status']
    search_fields = ['cust_tin_number', 'cust_pan_number']


class DispatchAdmin(admin.ModelAdmin):
    list_filter = ['group_name', 'city', 'product_code', 'product_category']
    search_fields = ['group_name', 'city', 'product_code', 'product_category']


# Register your models here.
admin.site.register(productForm, ProductAdmin)
admin.site.register(customerRegistration, CustomerAdmin)
admin.site.register(dispatchOrder, DispatchAdmin)