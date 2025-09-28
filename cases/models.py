from django.db import models

# Create your models here.
from django.db import models
from users.models import ClientProfile, LawyerProfile
from categories.models import Category

class Case(models.Model):
    RESULT_CHOICES = [
        ("pending", "در حال پیگیری"),
        ("success", "موفق"),
        ("failed", "ناموفق"),
    ]

    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name="cases")
    lawyer = models.ForeignKey(LawyerProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="cases")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    result = models.CharField(max_length=20, choices=RESULT_CHOICES, default="pending")
    is_previous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.user.first_name} - {self.category.name if self.category else 'بدون دسته'}"