from django.shortcuts import render
from  django.http import HttpResponse
from .models.product import Product
# Create your views here.

def homepage(request):
    prds=Product.get_all_products()
    return render(request,'Index/Index.html', {"Products":prds})
