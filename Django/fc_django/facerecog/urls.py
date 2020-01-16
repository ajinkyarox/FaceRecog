# pages/urls.py
from django.urls import path

from .views import *
from facerecog import views

urlpatterns = [
    path('', homePageView, name='home'),
    path('empdetails', getEmpDetails, name='getEmpDetails'),
    path('addEmployee', addEmployee, name='addEmployee'),
    path('updateEmployee', updateEmployee, name='updateEmployee'),
    path('deleteEmployee', views.deleteEmployee),
    path('savePhoto', savePhoto, name='savePhoto')

]

