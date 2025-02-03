from django.shortcuts import render, redirect
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

    return render(request, 'register_civilian.html', {'form': form})

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

    return render(request, 'register_company.html', {'form': form})

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

    return render(request, 'register_rcd_manager.html', {'form': form})

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

    return render(request, 'register_operator.html', {'form': form})