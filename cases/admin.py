from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Case

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'lawyer', 'category', 'result', 'is_previous', 'created_at')
    list_filter = ('result', 'is_previous', 'category', 'lawyer', 'client')
    search_fields = ('client__user__username', 'lawyer__user__username', 'description')