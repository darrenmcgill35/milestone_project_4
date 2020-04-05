from django.urls import path
from .views import all_store


urlpatterns = [
    path('store/', all_store, name='store'),
]

