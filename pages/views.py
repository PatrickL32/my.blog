from django.shortcuts import render
#from django.views.generic import TemplateView


#class HomePageView(TemplateView):
#    template_name = 'pages/home.html'

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def search(request):
    return render(request, 'pages/search.html')

# Create your views here.
