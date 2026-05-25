from django.urls import path
 
from .views import index, cart, product_detail

urlpatterns = [
    path("", index, name="index"),
    path("cart/", cart, name="cart"),
    path("product_detail/<int:id>", product_detail, name="product_detail")
]
