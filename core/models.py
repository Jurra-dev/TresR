from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Civilian (models.Model):
    first_name = models.CharFieldnull(null = False, blank = False)
    last_name = models.CharField(null = False, blank = False)
    phone_number = PhoneNumberField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)


# Create your models here.
