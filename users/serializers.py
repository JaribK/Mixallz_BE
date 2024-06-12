from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username', 'email', 'points', 'is_logged_in', 'is_activated', 'last_login', 'date_joined']