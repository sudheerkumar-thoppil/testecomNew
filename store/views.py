from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def storepage(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})
