from django.urls import path
from .views import (products, checkout, home)
from django.contrib.auth.urls import urlpatterns

app_name = 'store'

urlpatterns = [
    path('', home, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('products/', products, name='products'),
]
