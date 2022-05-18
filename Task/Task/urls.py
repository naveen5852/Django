from rest_framework.authtoken import views
from django.urls import path,include
from django.contrib import admin


urlpatterns = [
    path('api-auth-token/',views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('',include('login_api.urls')),
]
