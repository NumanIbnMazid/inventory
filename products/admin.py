from django.contrib import admin
from .models import Product, Order, OrderLine

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'quantity', 'price', 'created_at']

    class Meta:
        model = Product


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'total', 'order_date']

    class Meta:
        model = Order


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order', 'product', 'created_at']

    class Meta:
        model = OrderLine


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
