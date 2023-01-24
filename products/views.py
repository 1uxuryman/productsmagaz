import re

from django.shortcuts import HttpResponse,Http404
from django.shortcuts import render
from products.models import *




# Create your views here.
from products.models import Product


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = {'products': products}
        return render(request, 'products/product.html', context=data)


def product_detail_view(request,id):
        if request.method == 'GET':
            try:
                detail = Product.objects.get(id=id)
            except:
                raise Http404('Эу мындай бет жок эшек')
            context = {
                'product_detail': detail,
                'review': Review.objects.filter(product_id=id)
            }

            return render(request, 'products/detail.html', context=context)


