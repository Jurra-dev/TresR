# filepath: /C:/Herramientas/3R/project/TresR/core/tests.py
from django.test import TestCase
from .models import Civilian, Company, RcdManager, LogisticOperator

class CivilianModelTest(TestCase):
    def test_string_representation(self):
        civilian = Civilian(first_name="John", last_name="Doe")
        self.assertEqual(str(civilian), "John Doe")

class CompanyModelTest(TestCase):
    def test_string_representation(self):
        company = Company(company_name="Acme Corp")
        self.assertEqual(str(company), "Acme Corp")
