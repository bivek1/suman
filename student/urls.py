from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('dologin', views.dologin, name="dologin"),
    path('logout', views.log, name = "logout"),
    path('PricipalAdmin', views.dashBoard, name="adminHome"),
    path('addStaff', views.addStaff, name ="addStaff"),
    path('staffList', views.staffList, name="staffList"),
    path('addStudent', views.addStudent, name ="addStudent"),
    path('studentList', views.studentList, name = "studentList"),
    path('sendEmail', views.sendEmail, name = "sendEmail"),
    path('staffDashboard', views.staffDashboard , name="staffDashboard"),
    path('searchReport', views.SearchReport, name = "searchReport"),
    path('sendsms', views.sms, name = "sms"),
    path('liveattendance', views.attendace, name = "attendance"),
]
