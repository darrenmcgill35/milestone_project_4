from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart


urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('adjust_cart/', adjust_cart, name='adjust_cart'),
]


