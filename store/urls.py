from django.urls import path
from .views import all_stores


urlpatterns = [
    path('store/', all_stores, name='stores'),
]

