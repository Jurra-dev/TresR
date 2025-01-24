from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Civilian (models.Model):
    cc = models.IntegerField(null=False, blank=False, primary_key=True, default=0)
    first_name = models.CharField(null = False, blank = False, max_length = 140)
    last_name = models.CharField(null = False, blank = False, max_length = 140)
    phone_number = PhoneNumberField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']

class Company (models.Model):
    nit = models.IntegerField(null=False, blank=False, primary_key=True, default=0)
    company_name = models.CharField(null = False, blank = False, max_length = 140)
    representative_name = models.CharField(null = False, blank = False, max_length = 140)
    representative_id = models.IntegerField(null = False, blank = False, default=0)
    email = models.EmailField(null = False, blank = False)
    phone_number = PhoneNumberField(null = False, blank = False)
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        ordering = ['company_name']

class RcdManager (models.Model):
    #d = models.IntegerField(null=False, blank=False, primary_key=True, default=0)
    #representative_id = models.IntegerField(null = False, blank = False, default=0)
    name = models.CharField(null=False, blank=False, max_length=140)
    representative_name = models.CharField(null=False, blank=False, max_length=140)
    phone_number = PhoneNumberField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    office_address = models.CharField(null=False, blank=False, max_length=255)
    main_address = models.CharField(null=False, blank=False, max_length=255)
    city = models.CharField(null=False, blank=False, max_length=140)
    is_storage = models.BooleanField(null=False, blank=False, default=False)
    is_explotation = models.BooleanField(null=False, blank=False, default=False)
    is_collection_transport = models.BooleanField(null=False, blank=False, default=False)
    storage_capacity = models.IntegerField(null=False, blank=True, default=0)
    explotation_capacity = models.IntegerField(null=False, blank=True, default=0)
    final_disposition_capacity = models.IntegerField(null=False, blank=True, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class LogisticOperator (models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True, default=0)
    #representative_id = models.IntegerField(null = False, blank = False, default=0)
    name = models.CharField(null=False, blank=False, max_length=140)
    representative_name = models.CharField(null=False, blank=False, max_length=140)
    phone_number = PhoneNumberField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    office_address = models.CharField(null=False, blank=False, max_length=255)
    main_address = models.CharField(null=False, blank=False, max_length=255)
    activity = models.CharField(null=False, blank=False, max_length=140)
    city = models.CharField(null=False, blank=False, max_length=140)
    storage_capacity = models.IntegerField(null=False, blank=True, default=0)
    explotation_capacity = models.IntegerField(null=False, blank=True, default=0)
    final_disposition_capacity = models.IntegerField(null=False, blank=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
