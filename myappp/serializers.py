from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'phone', 'degree', 'school',
                  'university', 'summary', 'previous_work', 'skills',
                   'owner_username']
        read_only_fields = ['id']