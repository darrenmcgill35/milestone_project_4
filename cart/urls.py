from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart


urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/(<int:store_id>/)', add_to_cart, name='add_to_cart'),
    path('cart/adjust/<int:store_id>/', adjust_cart, name='adjust_cart'),
]


