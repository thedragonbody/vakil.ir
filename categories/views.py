from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from django.db.models import Q

# لیست همه دسته‌بندی‌ها و ساجست
class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Category.objects.filter(name__icontains=query)
        return Category.objects.all()