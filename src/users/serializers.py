from rest_framework import serializers
from .models import user

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = (
            'id', 'first_name', 'last_name', 'country_code', 'phone_number',
            'gender', 'birthdate', 'status'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }