from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'price_at_order', 'quantity', 'total_price')

    def total_price(self, obj):
        return obj.total_price() if obj.pk else 0
    total_price.short_description = 'Сумма'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status', 'total_price')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'phone', 'address')
    readonly_fields = ('created_at', 'total_price')
    inlines = [OrderItemInline]

    def total_price(self, obj):
        return obj.total_price()
    total_price.short_description = 'Сумма'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price_at_order', 'total_price')
    list_filter = ('order__status', 'order__created_at')
    search_fields = ('order__id', 'product__name')

    def total_price(self, obj):
        return obj.total_price()
    total_price.short_description = 'Сумма'