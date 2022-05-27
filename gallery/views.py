from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html')

def search_category(request):

    return render(request, 'search.html')