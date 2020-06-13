from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    product0=Product.objects.order_by('-id')[4]
    product1=Product.objects.order_by('-id')[1]
    product2=Product.objects.order_by('-id')[2]
    products=Product.objects.all()
    context={
        'product0':product0,
        'product1':product1,
        'product2':product2,
        'products':products
    }
    return render(request,'index.html',context)


def new(request):
    return HttpResponse('<h1>new</h1>')
