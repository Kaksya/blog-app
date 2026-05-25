from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    return render(request, "blog.html")

def about(request):
    return render(request, "about.html")
