from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(OrderItems)
admin.site.register(Category)
