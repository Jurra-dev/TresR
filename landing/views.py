from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CivilianForm, CompanyForm, RcdManagerForm, LogisticOperatorForm

# Create your views here.
def home(request):
    return render(request, 'landing/home.html')

def register_civilian(request):
    if request.method == 'POST':
        form = CivilianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after successful registration
        else:
            print(form.errors)
    else:
        form = CivilianForm()

    return render(request, 'register_form.html', {
        'form': form,
        'title': 'Registro de Civil',
        'submit_button_text': 'Registrar Civil'
    })

def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after successful registration
        else:
            print(form.errors)
    else:
        form = CompanyForm()

    return render(request, 'register_form.html', {
        'form': form,
        'title': 'Registro de Persona jurídica o Empresa',
        'submit_button_text': 'Registrar Compañía'
    })

def register_rcd_manager(request):
    if request.method == 'POST':
        form = RcdManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after successful registration
        else:
            print(form.errors)
    else:
        form = RcdManagerForm()

    return render(request, 'register_form.html', {
        'form': form,
        'title': 'Registro de Gestor Ambiental',
        'submit_button_text': 'Registrar Entidad'
    })

def register_operator(request):
    if request.method == 'POST':
        form = LogisticOperatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after successful registration
        else:
            print(form.errors)
    else:
        form = LogisticOperatorForm()

    return render(request, 'register_form.html', {
        'form': form,
        'title': 'Registro de Equipos para excavación, demolición y transporte',
        'submit_button_text': 'Registrar Operador'
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Inicia sesión
            return redirect('dashboard')  # Redirige al home después del login
        else:
            print(form.errors)  # Opcional: imprime errores en la consola
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirige al login después del logout