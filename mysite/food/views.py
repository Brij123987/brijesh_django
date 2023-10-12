from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import Item
from food.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.

# Function based index view
#  -------------------------------------------------------------------------------------


def index(request):

    if request.user.is_superuser:
        itemlist = Item.objects.all()

    elif request.user.is_authenticated and request.user.profile.user_type == 'Rest':
        itemlist = Item.objects.filter(for_user = request.user.username)

    elif request.user.is_authenticated and request.user.profile.user_type == 'Cust':
        itemlist = Item.objects.all()
    
    else:
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


# Class based create_item views
#  -------------------------------------------------------------------------------------

class CreateItem(CreateView):

    model = Item
    fields = ['prod_code','for_user','item_name','item_desc','items_price','item_image']
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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

    



