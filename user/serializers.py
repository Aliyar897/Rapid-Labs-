from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # type: ignore
from rest_framework import serializers
from .models import Team

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        return token

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'manager', 'members']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Team name must be at least 3 characters long.")
        return value
