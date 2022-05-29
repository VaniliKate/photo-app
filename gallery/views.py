from unicodedata import category
from django.shortcuts import render
from .models import Image, Category, Location

# Create your views here.

def index(request):

    gallery = Image.objects.all() [:6]
    return render(request, 'index.html', {'gallery':gallery})

def gallery(request):

    gallery = Image.objects.all()
    return render(request, 'gallery.html', {'gallery':gallery})

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        image = Category.objects.all().filter(category=search)
        return render(request, 'search.html', {"image":image})

