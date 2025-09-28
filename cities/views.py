from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import City
from .serializers import CitySerializer
from django.db.models import Q

class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return City.objects.filter(name__icontains=query)
        return City.objects.all()