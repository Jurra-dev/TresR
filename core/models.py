from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

class CustomUser(AbstractUser):
    is_civilian = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_rcd_manager = models.BooleanField(default=False)
    is_logistic_operator = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Civilian (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Relación con el usuario
    cc = models.IntegerField(null=False, blank=False, primary_key=True)
    first_name = models.CharField(null = False, blank = False, max_length = 140)
    last_name = models.CharField(null = False, blank = False, max_length = 140)
    phone_number = PhoneNumberField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']

class Company (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Relación con el usuario
    nit = models.IntegerField(null=False, blank=False, primary_key=True)
    company_name = models.CharField(null = False, blank = False, max_length = 140)
    representative_name = models.CharField(null = False, blank = False, max_length = 140)
    representative_id = models.IntegerField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    phone_number = PhoneNumberField(null = False, blank = False)
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        ordering = ['company_name']

class RcdManager (models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    representative_id = models.IntegerField(null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Relación con el usuario
    name = models.CharField(null=False, blank=False, max_length=140)
    representative_name = models.CharField(max_length=140, null=True, blank=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    office_address = models.CharField(max_length=255)
    main_address = models.CharField(null=False, blank=False, max_length=255)
    city = models.CharField(null=False, blank=False, max_length=140)
    is_storage = models.BooleanField(null=False, blank=False, default=False)
    is_exploitation = models.BooleanField(null=False, blank=False, default=False)
    is_collection_transport = models.BooleanField(null=False, blank=False, default=False)
    is_final_disposition = models.BooleanField(null=False, blank=False, default=False)
    storage_capacity = models.IntegerField(null=False, blank=True, default=0)
    exploitation_capacity = models.IntegerField(null=False, blank=True, default=0)
    final_disposition_capacity = models.IntegerField(null=False, blank=True, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class LogisticOperator (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Relación con el usuario
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    representative_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(null=False, blank=False, max_length=140)
    representative_name = models.CharField(null=True, blank=True, max_length=140)
    phone_number = PhoneNumberField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    office_address = models.CharField(max_length=255)
    # main_address = models.CharField(null=False, blank=False, max_length=255)
    # activity = models.CharField(null=False, blank=False, max_length=140)
    # city = models.CharField(null=False, blank=False, max_length=140)
    # storage_capacity = models.IntegerField(null=False, blank=True, default=0)
    # explotation_capacity = models.IntegerField(null=False, blank=True, default=0)
    # final_disposition_capacity = models.IntegerField(null=False, blank=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

