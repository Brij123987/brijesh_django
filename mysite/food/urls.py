from django.urls import path, include
from food import views

app_name = 'food'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('details/<int:item_id>/',views.index_1, name ='index_1'),
]