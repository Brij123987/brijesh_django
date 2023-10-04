from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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




