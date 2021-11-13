from .views import *
from django.urls import path


app_name = 'cart'


urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remov, name='cart_remove'),
]