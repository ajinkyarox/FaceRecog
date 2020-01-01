# pages/urls.py
from django.urls import path

from .views import homePageView,getEmpDetails

urlpatterns = [
    path('', homePageView, name='home'),
    path('empdetails', getEmpDetails, name='getEmpDetails')
]

