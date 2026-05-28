from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(OfferProduct)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Review)


class ProductImageAdmin(admin.TabularInline):
    model=ProductImage
    extra=1

@admin.register(Proeduct)
class ProductAdmin(admin.ModelAdmin):
    list_products=[
        'name', 'desc', 'price', 'category', 'subcategory', 'available',
    ]
    inlines=[ProductImageAdmin]
    

    

