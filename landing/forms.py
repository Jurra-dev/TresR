from django import forms
from core.models import Civilian, Company, RcdManager, LogisticOperator

class CivilianForm(forms.ModelForm):
    class Meta:
        model = Civilian
        fields = ['cc', 'first_name', 'last_name', 'email', 'phone_number']
        labels = {
            'cc': 'Número de identificación',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'phone_number': 'Teléfono',
        }
        widgets = {
            'cc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de identificación'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su teléfono'}),
        }
        error_messages = {
            'cc': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un número de identificación válido.',
            },
            'first_name': {
                'required': 'Este campo es obligatorio.',
            },
            'last_name': {
                'required': 'Este campo es obligatorio.',
            },
            'email': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una dirección de correo electrónico válida.',
            },
            'phone_number': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un número de teléfono válido.',
            },
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['nit', 'company_name', 'representative_name', 'representative_id', 'email', 'phone_number']
        labels = {
            'nit': 'NIT',
            'company_name': 'Nombre de la empresa',
            'representative_name': 'Nombre del representante',
            'representative_id': 'ID del representante',
            'email': 'Correo electrónico',
            'phone_number': 'Teléfono',
        }
        widgets = {
            'nit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el NIT de la empresa'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la empresa'}),
            'representative_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del representante'}),
            'representative_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el ID del representante'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
        }
        error_messages = {
            'nit': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un NIT válido.',
            },
            'company_name': {
                'required': 'Este campo es obligatorio.',
            },
            'representative_name': {
                'required': 'Este campo es obligatorio.',
            },
            'representative_id': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un ID válido.',
            },
            'email': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una dirección de correo electrónico válida.',
            },
            'phone_number': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un número de teléfono válido.',
            },
        }

class RcdManagerForm(forms.ModelForm):
    class Meta:
        model = RcdManager
        fields = [
            'name', 'representative_name', 'phone_number', 'email', 'office_address', 'main_address', 
            'city', 'is_storage', 'is_explotation', 'is_collection_transport', 
            'storage_capacity', 'explotation_capacity', 'final_disposition_capacity'
        ]
        labels = {
            'name': 'Nombre',
            'representative_name': 'Nombre del representante',
            'phone_number': 'Teléfono',
            'email': 'Correo electrónico',
            'office_address': 'Dirección de la oficina',
            'main_address': 'Dirección principal',
            'city': 'Ciudad',
            'is_storage': 'Es almacenamiento',
            'is_explotation': 'Es explotación',
            'is_collection_transport': 'Es transporte de recolección',
            'storage_capacity': 'Capacidad de almacenamiento',
            'explotation_capacity': 'Capacidad de explotación',
            'final_disposition_capacity': 'Capacidad de disposición final',
        }
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
        error_messages = {
            'name': {
                'required': 'Este campo es obligatorio.',
            },
            'representative_name': {
                'required': 'Este campo es obligatorio.',
            },
            'phone_number': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un número de teléfono válido.',
            },
            'email': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una dirección de correo electrónico válida.',
            },
            'office_address': {
                'required': 'Este campo es obligatorio.',
            },
            'main_address': {
                'required': 'Este campo es obligatorio.',
            },
            'city': {
                'required': 'Este campo es obligatorio.',
            },
            'is_storage': {
                'required': 'Este campo es obligatorio.',
            },
            'is_explotation': {
                'required': 'Este campo es obligatorio.',
            },
            'is_collection_transport': {
                'required': 'Este campo es obligatorio.',
            },
            'storage_capacity': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una capacidad válida.',
            },
            'explotation_capacity': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una capacidad válida.',
            },
            'final_disposition_capacity': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una capacidad válida.',
            },
        }

class LogisticOperatorForm(forms.ModelForm):
    class Meta:
        model = LogisticOperator
        fields = [
            'id', 'name', 'representative_name', 'phone_number', 'email', 'office_address', 
            'main_address', 'activity', 'city', 'storage_capacity', 
            'explotation_capacity', 'final_disposition_capacity'
        ]
        labels = {
            'id': 'ID',
            'name': 'Nombre',
            'representative_name': 'Nombre del representante',
            'phone_number': 'Teléfono',
            'email': 'Correo electrónico',
            'office_address': 'Dirección de la oficina',
            'main_address': 'Dirección principal',
            'activity': 'Actividad',
            'city': 'Ciudad',
            'storage_capacity': 'Capacidad de almacenamiento',
            'explotation_capacity': 'Capacidad de explotación',
            'final_disposition_capacity': 'Capacidad de disposición final',
        }
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
        error_messages = {
            'id': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un ID válido.',
            },
            'name': {
                'required': 'Este campo es obligatorio.',
            },
            'representative_name': {
                'required': 'Este campo es obligatorio.',
            },
            'phone_number': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un número de teléfono válido.',
            },
            'email': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una dirección de correo electrónico válida.',
            },
            'office_address': {
                'required': 'Este campo es obligatorio.',
            },
            'main_address': {
                'required': 'Este campo es obligatorio.',
            },
            'activity': {
                'required': 'Este campo es obligatorio.',
            },
            'city': {
                'required': 'Este campo es obligatorio.',
            },
            'storage_capacity': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una capacidad válida.',
            },
            'explotation_capacity': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una capacidad válida.',
            },
            'final_disposition_capacity': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una capacidad válida.',
            },
        }