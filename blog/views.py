from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("Welcome to my Blog")
    return render(request, 'blogs/index.html', {})