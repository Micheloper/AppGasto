from django.contrib import admin
from django.urls import path

from .views import Home,AgregarGastos, EditarGasto,DeleteCosto,AgregarPresupuesto,DeleteActivo,Userlogin,UserSignUp,userlogout

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login/',Userlogin.as_view(),name = 'login'),
    path('logout/',userlogout,name = 'logout'),
    path('signup/',UserSignUp.as_view(),name = 'signup'),

    path("agregarPresupuesto/", AgregarPresupuesto.as_view(),name="agregarPresupuesto"),


    path('agregarGastos/',AgregarGastos.as_view(),name='agregarGastos'),

    path('editarGasto/<int:pk>/', EditarGasto.as_view(),name='editarGasto'),

    path('deletecost/<int:pk>/',DeleteCosto.as_view(),name='deletecost'),

    path('deleteActivo/<int:pk>/',DeleteActivo.as_view(),name='deleteActivo'),

]
