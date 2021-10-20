from django.urls import path
from . import views
from ticketapp.views import ticket, statuss

urlpatterns = [
    path('register/', views.register, name= 'register'),
    path('', views.dashboard, name= 'dashboard'),
    path('empdashboard/', views.empdashboard, name= 'empdashboard'),
    path('login/', views.login, name= 'login'),
    path('ticket/', ticket, name= 'ticket'),
    path('status/', statuss, name= 'status'),
    #path('register/', views.employee_register.as_view()),
]
