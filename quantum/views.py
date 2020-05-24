from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    prod=Product.objects.all()
    param={'product':prod}
    return render(request,'index.html',param)