from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import Item
from food.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

# Function based index view
#  -------------------------------------------------------------------------------------


def index(request):
    itemlist = Item.objects.all()

    context = {
        'itemlist':itemlist
    }
    return render(request, 'food/index.html', context)


# Class based index views
#  -------------------------------------------------------------------------------------


class IndexClassView(ListView):

    model = Item
    context_object_name = 'itemlist'

    template_name = 'food/index.html' 



# Function based index_1 view
#  -------------------------------------------------------------------------------------


def index_1(request, item_id):
    item = Item.objects.get(pk = item_id)

    context = {
        'item':item
    }
    return render(request, 'food/detail.html', context)



# Class based index views
#  -------------------------------------------------------------------------------------

class FoodDetail(DetailView):

    model = Item
    context_object_name = 'item'
    template_name = 'food/detail.html'




# Function based create view
#  -------------------------------------------------------------------------------------


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form':form
    }

    return render(request, 'food/item-form.html', context)


# Function based update_item view
#  -------------------------------------------------------------------------------------


def update_item(request, id):
    item = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form' : form
    }

    return render(request, 'food/item-form.html', context)


# Function based delete_item view
#  -------------------------------------------------------------------------------------


def delete_item(request, id):
    item = Item.objects.get(pk = id)

    context = {
        'item' : item
    }

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', context)

    



