from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Case
from .serializers import CaseSerializer

# لیست پرونده‌ها برای کاربر لاگین شده (موکل)
class ClientCaseListView(generics.ListAPIView):
    serializer_class = CaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Case.objects.filter(client__user=self.request.user)

# لیست پرونده‌ها برای وکیل
class LawyerCaseListView(generics.ListAPIView):
    serializer_class = CaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Case.objects.filter(lawyer__user=self.request.user)