from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
admin.site.register(OfferProduct)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Review)

admin.site.site_title='Myshop Admin'
admin.site.site_header='django project'
admin.site.index_title='MYSHOP'


class ProductImageAdmin(admin.TabularInline):
    model=ProductImage
    extra=1

@admin.register(Proeduct)
class ProductAdmin(admin.ModelAdmin):
    # list_display=['name', 'desc', 'price', 'category', 'subcategory', 'available']
    list_display=['id','name', 'desc', 'price', 'category', 'subcategory', 'available', 'display_image']
    # list_display_links=['name']
    list_editable=['name']
    list_filter=['price', 'category']
    search_fields=['name']
    ordering=  ['name']
    inlines=[ProductImageAdmin]
    
    def display_image(self,obj):
        if obj.image:
            return format_html('<img src="{}" height="80px" width="80px">',obj.image.url)

    

