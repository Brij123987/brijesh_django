from django.urls import path, include
from food import views

app_name = 'food'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('details/<int:item_id>/',views.index_1, name ='index_1'),
    path('add/', views.create_item, name='create_item'),
    path('update/<int:id>/',views.update_item, name="update_item"),
    path('delete/<int:id>/',views.delete_item, name='delete_item'),
]