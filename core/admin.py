from django.contrib import admin
from .models import OfferProduct, Category, SubCategory, Proeduct

# Register your models here.
admin.site.register(OfferProduct)
admin.site.register(Category)
admin.site.register(SubCategory)

@admin.register(Proeduct)
class Product(admin.ModelAdmin):
    list_products=[
        'name', 'desc', 'price', 'category', 'subcategory', 'available',
    ]