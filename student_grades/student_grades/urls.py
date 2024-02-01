from django.urls import path
from app_sheet_reader import views

urlpatterns = [
    #rota,view responsavel,nome de referencia
    path('',views.home,name='home'),
    path('sheet_function/', views.sheet_function, name='sheet_function')
]
