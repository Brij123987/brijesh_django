from users import views
from django.urls import path

app_name = 'users'

urlpatterns = [

  # Orders
  path('orders/<int:id>/<int:pdcd>/<str:user>/',views.Orders, name='orders'),

  #Updating Customer Order
  path('upd_orders/<int:id>/<int:upd_order_id>/',views.update_orders, name='upd_orders'),

  # Customer Rating and Feedback view
  path('crf/<int:it_id>/<int:pc>/',views.CustRatFeed, name='CusRatFeed'),


  #updating Customer Ratings and Feedback
  path('crf_upd/<int:details_id>/<int:crf_id>/',views.update_crf, name='upd_crf'),

  #Delete Customer Rating and Feedback
  path('crf_delete/<int:details_id>/<int:crf_id>/',views.delete_crf, name='upd_delete'),

]

