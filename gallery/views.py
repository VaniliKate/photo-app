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
    if 'image' in request.GET and request.GET["image"]:
        search_term  =  request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message  = f"{search_term}"
        
        return render(request, 'search.html', {"message":message, "categories":searched_images})
    else:
        message = "You have not searched for any category"
        
        return render(request, 'search.html', {"message":message})

