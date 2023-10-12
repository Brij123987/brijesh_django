from django.urls import path, include
from food import views

app_name = 'food'

urlpatterns = [
    # Function based index view
    #  -------------------------------------------------------------------------------------
    path('home/', views.index, name='index'),


    # Class based index views
    #  -------------------------------------------------------------------------------------
    # path('home/',views.IndexClassView.as_view(), name='index'),


    # Function based index_1 view
    #  -------------------------------------------------------------------------------------
    # path('details/<int:item_id>/',views.index_1, name ='index_1'),


    # Class based index views
    #  -------------------------------------------------------------------------------------
    path('details/<int:pk>/',views.FoodDetail.as_view(), name='index_1'),


    # Function based create_item view
    #  -------------------------------------------------------------------------------------
    # path('add/', views.create_item, name='create_item'),


    # Class based index views
    #  -------------------------------------------------------------------------------------
    path('add/',views.CreateItem.as_view(), name='create_item'),

    
    # Function based update_item view
    #  -------------------------------------------------------------------------------------
    path('update/<int:id>/',views.update_item, name="update_item"),


    # Function based delete_item view
    #  -------------------------------------------------------------------------------------
    path('delete/<int:id>/',views.delete_item, name='delete_item'),
]