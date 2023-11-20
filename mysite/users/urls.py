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

]

