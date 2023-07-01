from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('patients/', views.getAddPatients),
    path('patients/<str:pk>/', views.modifyPatient),
]