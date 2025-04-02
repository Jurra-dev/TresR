# landing/urls.py
from django.urls import path
from . import views as control_panel_views

urlpatterns = [
     path('', control_panel_views.dashboard, name='dashboard'),  # Ruta para la landing page
    # path('register/civilian/', views.register_civilian, name='register_civilian'), 
    # path('register/company/', views.register_company, name='register_company'),
    # path('register/rcd_manager/', views.register_rcd_manager, name='register_rcd_manager'),
    # path('register/operator/', views.register_operator, name='register_operator'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
]
