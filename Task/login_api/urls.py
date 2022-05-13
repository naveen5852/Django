from django.urls import path
from . views import *


urlpatterns = [
    path('signup/', Signup.as_view(), name='Signup'),
    path('login/', Login.as_view(),name='Login'),
    path('employee/', EmployeeEntry.as_view(),name='Employee'),
    path('get-employee/<int:pk>/',EmployeeUpdate.as_view(),name='GetEmployee'),
    path('employeeAsset/',EmployeeAsset.as_view(),name='EmployeeAsset'),
    path('get-employeeAsset/<int:pk>/',EmployeeAssetUpdate.as_view(),name='GetEmployee'),
    path('employeeFamily/',EmployeeUpdate.as_view(),name='GetEmployee'),
    path('get-employeeFamily/<int:pk>/',EmployeeUpdate.as_view(),name='GetEmployee'),

]

