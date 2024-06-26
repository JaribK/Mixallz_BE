from rest_framework import serializers
from users.models import Users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username', 'points', 'email', 'is_logged_in', 'is_activated', 'is_superuser']