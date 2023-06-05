from django.shortcuts import render

# Create your views here.
def index(request):
    """Start screen for PlantStock"""
    return render(request, 'plants/index.html')