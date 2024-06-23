from django.contrib import admin
from .models import Product
from django.shortcuts import render

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_id", "description", "created", "updated"]
    list_filter = ["created", "updated"]
    actions = ["delete_with_images"]
    @admin.action
    def delete_with_images(self, request, queryset):
        for product in queryset:
            product.delete()
        self.message_user(request, "Objetos seleccionados y sus imagenes han sido borrados.")

admin.site.register(Product, ProductAdmin)