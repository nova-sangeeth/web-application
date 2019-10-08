from django.http import HttpResponse
from django.shortcuts import render

from .models import Items


def index(request):
    products = Items.objects.all()
    return render(request, 'products_pagedesign.html', {'Items': products})

    return HttpResponse('Hello world')


def new_item(request):
    return HttpResponse('new items')
