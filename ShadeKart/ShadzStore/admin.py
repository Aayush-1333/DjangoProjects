from django.contrib import admin

# Register your models here.
from .models import Product, Complaint, OrderDetail, OrderUpdate, UserAccount

admin.site.register(Product)
admin.site.register(Complaint)
admin.site.register(OrderDetail)
admin.site.register(OrderUpdate)
admin.site.register(UserAccount)
