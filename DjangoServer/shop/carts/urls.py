from django.urls import re_path as url
from shop.carts import views

urlpatterns = [
    url(r'carts', views.carts),
    url(r'carts_list', views.carts_list),
]