from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1 style="color:blue">This is an index view</h1>')
    
def index_1(request):
    return HttpResponse('<h1 style="color:Green">This is a details Page</h1>')