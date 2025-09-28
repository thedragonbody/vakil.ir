from rest_framework import serializers
from django.contrib.auth.models import User
from .models import LawyerProfile, ClientProfile
from categories.serializers import CategorySerializer
from cities.serializers import CitySerializer



class LawyerProfileSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    categories = CategorySerializer(many=True)
    success_rate = serializers.SerializerMethodField()

    class Meta:
        model = LawyerProfile
        fields = [
            'user', 'bio', 'experience_years', 'degree', 
            'leaderboard_score', 'city', 'categories', 'success_rate'
        ]

    def get_success_rate(self, obj):
        total_cases = obj.case_set.count()
        won_cases = obj.case_set.filter(result='won').count()
        return (won_cases / total_cases * 100) if total_cases > 0 else 0


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class LawyerRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = LawyerProfile
        fields = ['user', 'bio', 'experience_years', 'degree']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        lawyer = LawyerProfile.objects.create(user=user, **validated_data)
        return lawyer

class ClientRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ClientProfile
        fields = ['user', 'national_code']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        client = ClientProfile.objects.create(user=user, **validated_data)
        return client
    
class LawyerProfileSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = LawyerProfile
        fields = ['user', 'bio', 'experience_years', 'degree', 'leaderboard_score', 'city', 'categories']