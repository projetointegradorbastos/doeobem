from django.urls import path
from app_agendamentos import views

urlpatterns = [
    path('',views.home,name='home'),
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('registros/', views.registros, name='registros'),
]
