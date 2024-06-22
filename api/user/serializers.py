from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['categorie']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    employee = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'employee']

    def get_employee(self, obj):
        try:
            employee = Employee.objects.get(user=obj)
            serializer = EmployeeSerializer(employee)
            return serializer.data
        except Employee.DoesNotExist:
            return None

