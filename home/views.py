from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    # return render(request, 'pages/index.html')
    return render(request, 'pages/index.html')


def gallery(request):

    # Page from the theme 
    # return render(request, 'pages/index.html')
    return render(request, 'pages/gallery.html')