from django.shortcuts import render
from django.http import HttpResponse
from food.models import Item

# Create your views here.


def index(request):
    itemlist = Item.objects.all()

    context = {
        'itemlist':itemlist
    }
    return render(request, 'food/index.html', context)
    
def index_1(request):
    return HttpResponse('<h1 style="color:Green">This is a details Page</h1>')