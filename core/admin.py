# filepath: /C:/Herramientas/3R/project/TresR/core/admin.py
from django.contrib import admin
from .models import Civilian, Company, RcdManager, LogisticOperator

admin.site.register(Civilian)
admin.site.register(Company)
admin.site.register(RcdManager)
admin.site.register(LogisticOperator)
