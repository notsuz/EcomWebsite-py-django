from django.shortcuts import render
from .models import OfferProduct, Category, Proeduct, SubCategory, Brand
from django.db.models import Count,Prefetch

# Create your views here.

def index(request):
    offer=OfferProduct.objects.filter(is_available=True)
    category=Category.objects.annotate(count_sub=Count("subcategory")).prefetch_related(Prefetch('subcategory_set', queryset=\
        SubCategory.objects.annotate(product_count=Count('proeduct'))))
    
    sub_id=request.GET.get('subcategory')
    min=request.GET.get('min')
    max=request.GET.get('max')
    if sub_id and max and min:
        products=Proeduct.objects.filter(subcategory=sub_id, price__range=(min,max))
    elif sub_id:
        products=Proeduct.objects.filter(subcategory=sub_id)
    else:
        products=Proeduct.objects.all()
        
    brands=Brand.objects.annotate(product_count=Count('proeduct'))
    
    context={
        
        "offer":offer,
        "category": category,
        "products":products,
        "brands":brands,
    }
    return render(request, "core/index.html", context)


def cart(request):
    return render(request, "core/cart.html")

