from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'display_1/index.html')


def display_1_item(request):
    return render(request, 'display_1/display_1_item.html')
