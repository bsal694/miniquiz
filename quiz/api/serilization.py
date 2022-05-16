from rest_framework import serializers
from accounts.models import tempProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=tempProfile
        fields='__all__'