from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    images = Image.get_allImages()
    return render(request, 'index.html',{"images":images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        print(search_term)
        searched_images = Image.search_image_by_category(search_term)
        print(searched_images)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def nairobi(request):
    images = Image.search_image_by_location('nairobi')
    return render(request,'nairobi.html',{"images":images})

def tokyo(request):
    images = Image.search_image_by_location('tokyo')
    return render(request,'tokyo.html',{"images":images})
def rio(request):
    images = Image.search_image_by_location('rio')
    return render(request,'rio.html',{"images":images})

def berlin(request):
    images = Image.search_image_by_location('berlin')
    return render(request,'berlin.html',{"images":images})

