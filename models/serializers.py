from rest_framework import serializers
from .models import ListFeatures

class ListFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListFeatures
        fields = ['id', 'name', 'description', 'location', 'price', 'rating', 'category', 'is_active', 'created_at', 'updated_at']