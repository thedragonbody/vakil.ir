from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import LawyerRegisterSerializer, ClientRegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import LawyerProfile
from .serializers import LawyerProfileSerializer
from django.db.models import Q


class LawyerSearchView(generics.ListAPIView):
    serializer_class = LawyerProfileSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = LawyerProfile.objects.all()

        # فیلتر جستجو
        query = self.request.GET.get('q', None)
        city = self.request.GET.get('city', None)
        category = self.request.GET.get('category', None)
        leaderboard = self.request.GET.get('leaderboard', None)

        if query:
            queryset = queryset.filter(
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(categories__name__icontains=query)
            ).distinct()

        if city:
            queryset = queryset.filter(city__name__icontains=city)

        if category:
            queryset = queryset.filter(categories__name__icontains=category)

        if leaderboard == '1':
            queryset = queryset.order_by('-leaderboard_score')

        return queryset

class LawyerRegisterView(generics.CreateAPIView):
    serializer_class = LawyerRegisterSerializer
    permission_classes = [AllowAny]

class ClientRegisterView(generics.CreateAPIView):
    serializer_class = ClientRegisterSerializer
    permission_classes = [AllowAny]

class LawyerListView(generics.ListAPIView):
    serializer_class = LawyerProfileSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = LawyerProfile.objects.all()
        city = self.request.GET.get('city', None)
        category = self.request.GET.get('category', None)

        if city:
            queryset = queryset.filter(city__name__icontains=city)
        if category:
            queryset = queryset.filter(categories__name__icontains=category)

        return queryset