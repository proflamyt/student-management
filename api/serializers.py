from app.models import ClassMember  
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassMember
        fields = ['first_name', 'last_name', 'matric_number', 'attended']