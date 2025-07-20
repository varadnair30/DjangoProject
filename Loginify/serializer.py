from rest_framework import serializers
from .models import UserDetails

# class UserDetailsSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=50)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=12)

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields='__all__'

    