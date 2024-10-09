from django.contrib import admin
from storemodels import models
# Register your models here.

@admin.register(models.Product)
class StoreProduct(admin.ModelAdmin):
    list_display = 'name', 'description',

@admin.register(models.Category)
class CategoryStore(admin.ModelAdmin):
    list_display = 'name',

@admin.register(models.Customer)
class CategoryStore(admin.ModelAdmin):
    list_display = 'name', 'surname', 'email',


@admin.register(models.Order)
class CategoryStore(admin.ModelAdmin):
    list_display = 'customer', 'date_ordered', 'complete',

@admin.register(models.OrderItem)
class CategoryStore(admin.ModelAdmin):
    list_display = 'product', 'order', 'quantity',
