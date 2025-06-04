from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.db import models

#-----------------------------------------------------------------Additional Fucntions-----------------------------------------------------------------

def project_photo_upload_to(instance, filename): #This fucntion is used to upload the photo of a Project to its corresponding folder
    return f'projects/{instance.project.id}/photos/{filename}'

def project_document_upload_to(instance, filename): #This fucntion is used to upload the PDF Document of a Project to its corresponding folder
    return f'projects/{instance.project.id}/documents/{filename}'

#-----------------------------------------------------------------Models-----------------------------------------------------------------

class Project(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects'
    )  # Relación con el usuario

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Material(models.Model):
    name = models.CharField(max_length=255)
    usage = models.CharField(max_length=255) #Supply || Demand

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Supply(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='supplies')
    activities = models.CharField(max_length=255)
    material = models.ForeignKey('Material', on_delete=models.CASCADE, related_name='supplies')
    volume = models.FloatField()

class Demand(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='demands')
    activities = models.CharField(max_length=255)
    material = models.ForeignKey('Material', on_delete=models.CASCADE, related_name='demands')
    volume = models.FloatField()

class Photo(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to=project_photo_upload_to)
    uplided_at = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to=project_document_upload_to)
    type = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)