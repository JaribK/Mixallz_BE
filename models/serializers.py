from rest_framework import serializers
from .models import ListFeatures, Code, UserCodeRedemption

class ListFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListFeatures
        fields = ['id', 'name', 'description', 'location', 'price', 'rating', 'category', 'is_active', 'created_at', 'updated_at']

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['id','code', 'created_at']

class UserCodeRedemptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCodeRedemption
        fields = ['user', 'code', 'redeemed_at']