from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import LawyerProfile, ClientProfile

@admin.register(LawyerProfile)
class LawyerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'experience_years', 'leaderboard_score', 'degree')
    list_filter = ('city', 'categories')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'degree')
    filter_horizontal = ('categories',)

@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'national_code', 'city')
    list_filter = ('city',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'national_code')