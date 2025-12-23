from django.contrib import admin
from .models import Category, Product, Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'address', 'description')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'image', 'is_active')
        }),
        ('Контакты', {
            'fields': ('address', 'phone', 'email', 'website')
        }),
        ('Геолокация', {
            'fields': ('latitude', 'longitude'),
            'description': 'Координаты для отображения на карте. Можно найти на maps.google.com'
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier', 'price', 'in_stock')
    list_filter = ('category', 'supplier', 'in_stock')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'in_stock')