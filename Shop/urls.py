from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('shop/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    # path('logout/', views.logout_view, name='logout'),

]


# time 25