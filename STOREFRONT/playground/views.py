from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product,OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F

def Say_hello(request):
    product=Product.objects.filter(id__in=OrderItem.objects.values('product_id'))
    total=product.count()
     
     
    return render(request,'hello.html',{'name':'World','products':list(product),'total':total})

