from rest_framework import serializers

from school.models import TenantUser

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class AdminProfileSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(read_only=True)
    class Meta:
        model = TenantUser
        fields = '__all__'

    def create(self, validated_data):
        ...