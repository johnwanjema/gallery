from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    images = Image.get_allImages()
    return render(request, 'index.html',{"images":images})