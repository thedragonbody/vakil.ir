from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from cities.models import City
from categories.models import Category
from users.models import LawyerProfile, ClientProfile
from cases.models import Case

class APITestCases(TestCase):
    def setUp(self):
        self.client_api = APIClient()

        # ایجاد شهرها
        self.city1 = City.objects.create(name="تهران")
        self.city2 = City.objects.create(name="اصفهان")

        # ایجاد دسته‌بندی‌ها
        self.cat1 = Category.objects.create(name="خانواده")
        self.cat2 = Category.objects.create(name="کیفری")

        # ایجاد وکلا
        self.lawyer_user1 = User.objects.create_user(username="lawyer1", password="pass123")
        self.lawyer1 = LawyerProfile.objects.create(user=self.lawyer_user1, city=self.city1, experience_years=5, leaderboard_score=90)
        self.lawyer1.categories.add(self.cat1)

        self.lawyer_user2 = User.objects.create_user(username="lawyer2", password="pass123")
        self.lawyer2 = LawyerProfile.objects.create(user=self.lawyer_user2, city=self.city2, experience_years=3, leaderboard_score=80)
        self.lawyer2.categories.add(self.cat2)

        # ایجاد موکل و پرونده
        self.client_user = User.objects.create_user(username="client1", password="pass123")
        self.client_profile = ClientProfile.objects.create(user=self.client_user, national_code="1234567890", city=self.city1)
        self.case = Case.objects.create(client=self.client_profile, lawyer=self.lawyer1, category=self.cat1, description="پرونده تست", result="pending")

    def test_lawyer_list(self):
        # گرفتن لیست وکلا
        response = self.client_api.get("/api/users/")  # فرض کنیم یک endpoint برای لیست وکلا داریم
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(len(data) >= 2)

    def test_search_lawyer_by_city(self):
        # جستجو بر اساس شهر
        response = self.client_api.get("/api/users/?city=تهران")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(all(lawyer['city']['name'] == "تهران" for lawyer in data))

    def test_search_lawyer_by_category(self):
        # جستجو بر اساس دسته‌بندی
        response = self.client_api.get("/api/users/?category=خانواده")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(all("خانواده" in [c['name'] for c in lawyer['categories']] for lawyer in data))