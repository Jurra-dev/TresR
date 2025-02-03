from django import forms
from core.models import Civilian, Company, RcdManager, LogisticOperator

class CivilianForm(forms.ModelForm):
    class Meta:
        model = Civilian
        fields = ['cc', 'first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'cc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de identificación'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su teléfono'}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['nit', 'company_name', 'representative_name', 'representative_id', 'email', 'phone_number']
        widgets = {
            'nit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el NIT de la empresa'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la empresa'}),
            'representative_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del representante'}),
            'representative_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el ID del representante'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
        }

class RcdManagerForm(forms.ModelForm):
    class Meta:
        model = RcdManager
        fields = [
            'name', 'representative_name', 'phone_number', 'email', 'office_address', 'main_address', 
            'city', 'is_storage', 'is_explotation', 'is_collection_transport', 
            'storage_capacity', 'explotation_capacity', 'final_disposition_capacity'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'representative_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del representante'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
            'office_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección de la oficina'}),
            'main_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección principal'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad'}),
            'is_storage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_explotation': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_collection_transport': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'storage_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de almacenamiento'}),
            'explotation_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de explotación'}),
            'final_disposition_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de disposición final'}),
        }

class LogisticOperatorForm(forms.ModelForm):
    class Meta:
        model = LogisticOperator
        fields = [
            'id', 'name', 'representative_name', 'phone_number', 'email', 'office_address', 
            'main_address', 'activity', 'city', 'storage_capacity', 
            'explotation_capacity', 'final_disposition_capacity'
        ]
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'representative_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del representante'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
            'office_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección de la oficina'}),
            'main_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección principal'}),
            'activity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la actividad'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad'}),
            'storage_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de almacenamiento'}),
            'explotation_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de explotación'}),
            'final_disposition_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de disposición final'}),
        }