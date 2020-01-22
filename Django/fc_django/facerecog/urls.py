# pages/urls.py
from django.urls import path
from .views import getEmpDetails,addEmployee,updateEmployee,deleteEmployee,savePhoto,markAttendance,getAttendance,getMonthlyReport
from facerecog import views

urlpatterns = [

    path('empdetails', getEmpDetails, name='getEmpDetails'),
    path('addEmployee', addEmployee, name='addEmployee'),
    path('updateEmployee', updateEmployee, name='updateEmployee'),
    path('deleteEmployee', deleteEmployee),
    path('savePhoto', savePhoto, name='savePhoto'),
    path('markAttendance',markAttendance,name='markAttendance'),
    path('getAttendance',getAttendance,name='getAttendance'),
    path('getMonthlyReport',getMonthlyReport,name='getMonthlyReport')
]

