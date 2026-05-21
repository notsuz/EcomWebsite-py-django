from django.db import models
from cloudinary.models import CloudinaryField
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class OfferProduct(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    image=CloudinaryField("image")
    is_available=models.BooleanField(default=True)
    created_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class SubCategory(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Brand(models.Model):
    name=models.CharField(max_length=200)
    subcategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
        
    def __str__(self):
        return self.name
    
class Proeduct(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    desc = CKEditor5Field('Text', config_name='extends')
    image=CloudinaryField('image')
    available=models.BooleanField(default=True)
    stock=models.PositiveSmallIntegerField()
    mark_price=models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent=models.DecimalField(max_digits=4, decimal_places=2)
    price=models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    brands=models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name

    
    def save(self,  *args, **kwargs):
        self.name=self.name.capitalize()
        self.price=self.mark_price*(1-self.discount_percent/100)
        super().save(*args, **kwargs)
        
class ProductImage(models.Model):
    image=CloudinaryField("images")
    product=models.ForeignKey(Proeduct, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.name
    
