from django.contrib import admin
from storemodels import models
# Register your models here.

@admin.register(models.Product)
class StoreAdmin(admin.ModelAdmin):
    list_display = 'name', 'description',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = 'name', 'surname', 'email',


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'customer', 'date_ordered', 'complete',

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = 'product', 'order', 'quantity',
