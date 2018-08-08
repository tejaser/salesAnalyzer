from django.contrib import admin
from .models import productForm, customerRegistration, dispatchOrder

admin.site.register([productForm, customerRegistration, dispatchOrder])
# Register your models here.
