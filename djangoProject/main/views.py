from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def general_statistics(request):
    return render(request, 'main/statistics.html')