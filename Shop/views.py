from django.shortcuts import render
from Shop.models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})