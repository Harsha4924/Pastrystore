from . import views
from django.urls import path

app_name = 'pastry_store'

urlpatterns = [
    path("thankyou/",views.thankyou,name="thankyou"),
    path("payment/",views.payment,name="payment"),
    path("", views.home,name="home"),
    path("add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("update_cart/<int:myid>/<operator>", views.update_cart, name="update_cart"),
    path("cart/",views.my_cart, name="my_cart"),
    path("<str:category>/", views.item_detail,name="item_detail"),
]
