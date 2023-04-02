from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'get_image', 'get_thumbnail', 'description')
    search_fields = ('name', 'price', 'description')
    list_filter = ('name', 'price', 'description')
    readonly_fields = ('get_image', 'get_thumbnail')
    fieldsets = (
        (_('Ürün Bilgileri'), {'fields': ('name', 'price', 'description')}),
        (_('Ürün Resimleri'), {'fields': ('image', 'thumbnail')}),
    )
