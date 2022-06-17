from rest_framework import serializers
from .models import IssuList, Login

class IssuListSerializer(serializers.ModelSerializer):
    class Meta:
        model=IssuList 
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login 
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login 
        fields = 'FirstName','LastName','Email','IsActive','Roles'