from rest_framework import serializers
from users.models import Users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username', 'email', 'points', 'is_logged_in', 'is_activated', 'is_superuser']