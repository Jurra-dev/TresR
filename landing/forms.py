from django import forms
from core.models import CustomUser, Civilian, Company, RcdManager, LogisticOperator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
        label="Correo electrónico"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}),
        label="Contraseña"
    )

class CivilianForm(forms.ModelForm):
    # Campo para la contraseña
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese una contraseña'}),
        label="Contraseña"
    )

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
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número telefónico'}),
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

    def save(self, commit=True):
    # Crear el usuario relacionado
        user = CustomUser(
            username=self.cleaned_data['email'],  # Usa el email como nombre de usuario
            email=self.cleaned_data['email'],
            password=make_password(self.cleaned_data['password']),  # Encripta la contraseña
            is_civilian=True  # Marca al usuario como Civilian
        )
        if commit:
            user.save()

        # Crear el Civilian relacionado
        civilian = super().save(commit=False)
        civilian.user = user  # Relaciona el usuario con el Civilian
        if commit:
            civilian.save()
        return civilian

class CompanyForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}),
        label="Contraseña"
    )
    
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
            'representative_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el número de identificación del representante'}),
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

    def save(self, commit=True):
        user = CustomUser(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=make_password(self.cleaned_data['password']),
            is_company=True
        )
        if commit:
            user.save()

        company = super().save(commit=False)
        company.user = user
        if commit:
            company.save()
        return company

class RcdManagerForm(forms.ModelForm):

    is_legal_entity = forms.ChoiceField(
        choices=[('natural', 'Persona Natural'), ('legal', 'Persona Jurídica')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label="Tipo de Persona"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}),
        label="Contraseña"
    )

    class Meta:
        model = RcdManager
        fields = [
            'id', 'name', 
            'representative_name',
            'representative_id',
            'phone_number', 'email', 'office_address', 'main_address', 
            'city', 'is_storage', 'is_exploitation', 'is_collection_transport', 'is_final_disposition',
            'storage_capacity', 'exploitation_capacity', 'final_disposition_capacity'
        ]
        labels = {
            'id': 'Número de identificación o NIT',
            'name': 'Nombre de la empresa o representante legal',
            'representative_id': 'Número de identificación del representante legal',
            'representative_name': 'Nombre del representante',
            'phone_number': 'Teléfono',
            'email': 'Correo electrónico',
            'office_address': 'Dirección de la oficina (Si aplica)',
            'main_address': 'Dirección principal',
            'city': 'Ciudad',
            'is_storage': 'Es almacenamiento',
            'is_exploitation': 'Es explotación',
            'is_collection_transport': 'Es transporte de recolección',
            'is_final_disposition': 'Es disposición final',
            'storage_capacity': 'Capacidad de almacenamiento',
            'exploitation_capacity': 'Capacidad de explotación',
            'final_disposition_capacity': 'Capacidad de disposición final',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de identificación o NIT'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'representative_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el número de identificación del representante'}),
            'representative_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del representante'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
            'office_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección de la oficina'}),
            'main_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección principal'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad'}),
            'is_storage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_exploitation': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_collection_transport': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_final_disposition': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'storage_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de almacenamiento'}),
            'exploitation_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de explotación'}),
            'final_disposition_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de disposición final'}),
        }
        error_messages = {
            'name': {
                'required': 'Este campo es obligatorio.',
            },
            # 'representative_name': {
            #     'required': 'Este campo es obligatorio.',
            # },
            # 'representative_id': {
            #     'required': 'Este campo es obligatorio.',
            #     'invalid': 'Ingrese un número de identificación válido.'
            # },
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
            'is_exploitation': {
                'required': 'Este campo es obligatorio.',
            },
            'is_collection_transport': {
                'required': 'Este campo es obligatorio.',
            },
            'is_final_disposition': {
                'required': 'Este campo es obligatorio.',
            },
            'storage_capacity': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una capacidad válida.',
            },
            'exploitation_capacity': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una capacidad válida.',
            },
            'final_disposition_capacity': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese una capacidad válida.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        is_legal_entity = cleaned_data.get('is_legal_entity')
        if is_legal_entity == 'legal':
            if not cleaned_data.get('representative_name'):
                self.add_error('representative_name', 'Este campo es obligatorio para personas jurídicas.')
            if not cleaned_data.get('representative_id'):
                self.add_error('representative_id', 'Este campo es obligatorio para personas jurídicas.')
        return cleaned_data

    def save(self, commit=True):
        user = CustomUser(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=make_password(self.cleaned_data['password']),
            is_rcd_manager=True
        )
        if commit:
            user.save()

        rcd_manager = super().save(commit=False)
        rcd_manager.user = user
        if commit:
            rcd_manager.save()
        return rcd_manager

class LogisticOperatorForm(forms.ModelForm):

    is_legal_entity = forms.ChoiceField(
        choices=[('natural', 'Persona Natural'), ('legal', 'Persona Jurídica')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label="Tipo de Persona"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}),
        label="Contraseña"
    )

    class Meta:
        model = LogisticOperator
        fields = [
            'id', 'name',
            'representative_id',
            'representative_name',
            'phone_number', 'email', 'office_address', 
            # 'main_address', 
            # 'activity', 'storage_capacity', 
            # 'explotation_capacity', 'final_disposition_capacity',
            # 'city'
        ]
        labels = {
            'id': 'Número de identificación o NIT',
            'name': 'Nombre de la empresa o representante legal',
            'representative_id': 'Número de identificación del representante legal',
            'representative_name': 'Nombre del representante legal',
            'phone_number': 'Teléfono',
            'email': 'Correo electrónico',
            'office_address': 'Dirección de la oficina',
            # 'main_address': 'Dirección principal',
            # 'activity': 'Actividad',
            # 'city': 'Ciudad',
            # 'storage_capacity': 'Capacidad de almacenamiento',
            # 'explotation_capacity': 'Capacidad de explotación',
            # 'final_disposition_capacity': 'Capacidad de disposición final',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de identificación o NIT'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'representative_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el número de identificación del representante'}),
            'representative_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del representante legal'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un número de teléfono de contacto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'office_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección de la oficina (si aplica)'}),
            # 'main_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección principal del pr'}),
            # 'activity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la actividad'}),
            # 'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad'}),
            # 'storage_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de almacenamiento'}),
            # 'explotation_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de explotación'}),
            # 'final_disposition_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad de disposición final'}),
        }
        error_messages = {
            'id': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un ID válido.',
            },
            'name': {
                'required': 'Este campo es obligatorio.',
            },
            # 'representative_id': {
            #     'required': 'Este campo es obligatorio.',
            # },
            # 'representative_name': {
            #     'required': 'Este campo es obligatorio.',
            # },
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
            # 'main_address': {
            #     'required': 'Este campo es obligatorio.',
            # },
            # 'activity': {
            #     'required': 'Este campo es obligatorio.',
            # },
            # 'city': {
            #     'required': 'Este campo es obligatorio.',
            # },
            # 'storage_capacity': {
            #     'required': 'Este campo es obligatorio.',
            #     'invalid': 'Ingrese una capacidad válida.',
            # },
            # 'explotation_capacity': {
            #     'required': 'Este campo es obligatorio.',
            #     'invalid': 'Ingrese una capacidad válida.',
            # },
            # 'final_disposition_capacity': {
            #     'required': 'Este campo es obligatorio.',
            #     'invalid': 'Ingrese una capacidad válida.',
            # },
        }

    def clean(self):
        cleaned_data = super().clean()
        is_legal_entity = cleaned_data.get('is_legal_entity')
        if is_legal_entity == 'legal':
            if not cleaned_data.get('representative_name'):
                self.add_error('representative_name', 'Este campo es obligatorio para personas jurídicas.')
            if not cleaned_data.get('representative_id'):
                self.add_error('representative_id', 'Este campo es obligatorio para personas jurídicas.')
        return cleaned_data
    
    def save(self, commit=True):
        user = CustomUser(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=make_password(self.cleaned_data['password']),
            is_logistic_operator=True
        )
        if commit:
            user.save()

        logistic_operator = super().save(commit=False)
        logistic_operator.user = user
        if commit:
            logistic_operator.save()
        return logistic_operator