from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import CusOrders
from users.forms import CusOrdersUpd

# Create your views here.

def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data.get('username')
      messages.success(request, f'Welcome {username}, your account has been successfully created. Now you may log in.')
      form.save()
      return redirect('login')

  else:
    form = RegisterForm()

    context = {
      'form':form
    }

    return render(request, 'users/register.html', context)
  
def login_view(request):

  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    
    if user is None:
      messages.success(
        request,
        'Invalid Login, try again'
      )
      return redirect('login')

    elif user.is_superuser:
      login(request, user)
      messages.success(
        request,
        f'Welcome Superuser {request.user.username}, you have been successfully logged in.'
      )
      return redirect('food:index')

    elif user is not None:
      login(request, user)
      messages.success(
        request,
        f'Welcome {request.user.username}, you have been successfully logged in.'
      )
      return redirect('food:index')
    


  return render(request, 'users/login.html')


def logout_view(request):
  
  messages.success(
  request,
  f'{request.user.username}, you have successfully logged out.'
  )
  logout(request)
  return redirect('food:index')



@login_required
def profilepage(request):
  
  return render(request, 'users/profile.html')


def Orders(request, id, pdcd, user):

  context = {
    'pdcd':pdcd,
    'user':user
  }

  if request.method == 'POST':
    
    obj_CusOrders = CusOrders(
      prod_code = pdcd,
      user = user,
      quantity = request.POST.get('qty')

    )

    obj_CusOrders.save()

    return redirect('food:index_1', item_id=id)
    

  return render(request, 'users/orders.html', context)
  

def update_orders(request, id, upd_order_id):
# Customer Order Object
  coo = CusOrders.objects.get(order_id=upd_order_id)
  form = CusOrdersUpd(request.POST or None, instance=coo)

  context = {
    'form':form
  }
  if request.method == 'POST':
    form.instance.order_id = coo.order_id
    form.instance.prod_code = coo.prod_code
    form.instance.user = request.user.username
    form.save()
    return redirect('food:index_1',item_id = id)

  return render(request,'users/orders_upd.html',context)



