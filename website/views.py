from operator import index
from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')
