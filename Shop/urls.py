from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('shop/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]