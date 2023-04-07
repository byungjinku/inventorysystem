# product/urls.py
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home'), # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('product/', views.product, name='product'), # 127.0.0.1:8000/product 과 views.py 폴더의 product 함수 연결
    path('add/', views.add_product, name='add_product'),
    path('add_quantity/', views.add_quantity, name='add_quantity'),
    path('remove_quantity/', views.remove_quantity, name='remove_quantity'),
    path('total_quantity/', views.total_quantity, name='total_quantity'),
    path('product_list/', views.product_list, name='product_list'),
]