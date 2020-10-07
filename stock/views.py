from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')
def about(request):
    return render(request, 'frontend/about.html')
def tracks(request):
    return render(request, 'frontend/tracks.html')
def contact(request):
    return render(request, 'frontend/contact.html')
