# landing/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la landing page
    path('register/civilian/', views.register_civilian, name='register_civilian'), 
    path('register/company/', views.register_company, name='register_company'),
    path('register/rcd_manager/', views.register_rcd_manager, name='register_rcd_manager'),
    path('register/operator/', views.register_operator, name='register_operator'),
]
