from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def search(request):
    return render(request, 'pages/search.html')

# Create your views here.
