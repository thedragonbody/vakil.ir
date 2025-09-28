from rest_framework import serializers
from .models import Case
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer

class CaseSerializer(serializers.ModelSerializer):
    client = UserSerializer(source='client.user', read_only=True)
    lawyer = UserSerializer(source='lawyer.user', read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Case
        fields = ['id', 'client', 'lawyer', 'category', 'description', 'result', 'is_previous', 'created_at']