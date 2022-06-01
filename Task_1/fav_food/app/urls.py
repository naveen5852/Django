from django.urls import path
from .views import *

urlpatterns = [

    path('user/',FavFood.as_view({'get':'list','post':'create'}),name='UserDetail'),
    path('',RandomData.as_view(),name='FavFood'),

]
