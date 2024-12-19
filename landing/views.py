from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'landing/home.html')

def register_civilian(request):
    return render(request, 'landing/register_civilian.html')

def register_company(request):
    return render(request, 'landing/register_company.html')

def register_rcd_manager(request):
    return render(request, 'landing/register_rcd_manager.html')

def register_operator(request):
    return render(request, 'landing/register_operator.html')