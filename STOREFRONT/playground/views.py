from django.shortcuts import render
from django.http import HttpResponse

def Say_hello(request):
    return render(request,'hello.html',{'name':'PraiseTech'})

