from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),                              #empty quotes represent root(main) website
    path('register', views.register, name = 'register'),
    path('queue details', views.view_queue, name = 'queue details'),    #name is used in redirect and render. first argument gets displayed on website url
    path('otp/<str:phoneNumber>/', views.otp, name = 'otp'),            #sending phone number to next webpage (from registration to otp page)
    path('login', views.login, name = 'login'),
    path('employee', views.employee, name = 'employee'),
    path('logout', views.logout, name = 'logout'),
    path('selectCounter', views.selectCounter, name = 'selectCounter'),
]