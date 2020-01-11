# pages/urls.py
from django.urls import path

from .views import *

urlpatterns = [
    path('', homePageView, name='home'),
    path('empdetails', getEmpDetails, name='getEmpDetails'),
    path('addEmployee', addEmployee, name='addEmployee'),
    path('updateEmployee', updateEmployee, name='updateEmployee'),
    path('deleteEmployee', deleteEmployee, name='deleteEmployee')

]

