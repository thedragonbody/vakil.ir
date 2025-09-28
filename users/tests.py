from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from cities.models import City
from categories.models import Category
from users.models import LawyerProfile, ClientProfile
from cases.models import Case

class SimpleAPITest(TestCase):
    def setUp(self):
        self.client_api = APIClient()
        # ایجاد شهر
        self.city = City.objects.create(name="تهران")
        # ایجاد دسته‌بندی
        self.category = Category.objects.create(name="خانواده")
        # ایجاد کاربر وکیل
        self.lawyer_user = User.objects.create_user(username="lawyer1", password="pass123")
        self.lawyer = LawyerProfile.objects.create(user=self.lawyer_user, city=self.city, experience_years=5)
        self.lawyer.categories.add(self.category)
        # ایجاد کاربر موکل
        self.client_user = User.objects.create_user(username="client1", password="pass123")
        self.client_profile = ClientProfile.objects.create(user=self.client_user, national_code="1234567890", city=self.city)
        # ایجاد پرونده
        self.case = Case.objects.create(client=self.client_profile, lawyer=self.lawyer, category=self.category, description="پرونده تست", result="pending")

    def test_lawyer_profile(self):
        self.assertEqual(self.lawyer.user.username, "lawyer1")
        self.assertEqual(self.lawyer.city.name, "تهران")
        self.assertIn(self.category, self.lawyer.categories.all())

    def test_client_profile(self):
        self.assertEqual(self.client_profile.user.username, "client1")
        self.assertEqual(self.client_profile.national_code, "1234567890")

    def test_case(self):
        self.assertEqual(self.case.client.user.username, "client1")
        self.assertEqual(self.case.lawyer.user.username, "lawyer1")
        self.assertEqual(self.case.category.name, "خانواده")