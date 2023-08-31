from django.urls import path, include
from food import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('details/',views.index_1, name ='index_1'),
]