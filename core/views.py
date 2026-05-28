from django.shortcuts import render, get_object_or_404, redirect
from .models import OfferProduct, Category, Proeduct, SubCategory, Brand
from django.db.models import Count,Prefetch
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm


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
    
    paginator=Paginator(products,1)
    page_n=request.GET.get("page")
    data=paginator.get_page(page_n)
    total=data.paginator.num_pages
    context={
        
        "offer":offer,
        "category": category,
        "products":products,
        "brands":brands,
        "data":data,
        # "num":[i+1 for i in range(total)] #list sth
        "num": paginator.get_elided_page_range(number=data.number, on_each_side=1, on_ends=1)
    }
    return render(request, "core/index.html", context)


def cart(request):
    return render(request, "core/cart.html")

# @login_required(login_url='log_in')
def product_detail(request, id):
    product=get_object_or_404(Proeduct,id=id)
    reviews=product.reviews.all()
    
    review_count = reviews.count()
    
    form=ReviewForm()
    if request.method=="POST":
        form=ReviewForm(data=request.POST)
        if form.is_valid():
            review=form.save(commit=False) #delays the submission
            review.user=request.user
            review.product=product
            review.save()
            return redirect('product_detail', id=product.id)    
    
    
    context={
        'product':product,
        'form': form,
        "reviews":reviews,
        'review_count': review_count,
        'range':range(1,6)
    }
    return render(request, "core/product_detail.html", context)

