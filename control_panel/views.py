from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
#from landing.forms import CivilianForm, CompanyForm, RcdManagerForm, LogisticOperatorForm

# Create your views here.
@login_required
def dashboard(request):
    # Determina el tipo de usuario y pasa información al contexto
    user = request.user
    context = {
        'is_civilian': user.is_civilian,
        'is_company': user.is_company,
        'is_rcd_manager': user.is_rcd_manager,
        'is_logistic_operator': user.is_logistic_operator,
    }
    return render(request, 'dashboard.html', context)