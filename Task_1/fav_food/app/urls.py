from django.urls import path
from .views import *

urlpatterns = [

    path('',FavFood.as_view(),name = 'FavFood'),
]
