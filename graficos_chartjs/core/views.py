from django.shortcuts import render

# Create your views here.
def home(request):
    render(request, 'core/home.html')