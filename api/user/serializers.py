from django.contrib.auth.models import User
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['categorie']

class UserSerializer(
    WritableNestedModelSerializer,
    serializers.ModelSerializer
):
    employee = EmployeeSerializer(many=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name',  'is_staff', 'employee',]

    def update(self, instance, validated_data):
        if not instance.is_staff:
            employee_data = validated_data.pop('employee', {})
            employee_data.pop('categorie', None)
            validated_data.pop('username', None)
            instance = super().update(instance, validated_data)
        return instance
