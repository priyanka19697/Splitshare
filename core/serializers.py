from django.contrib.auth.models import User
from rest_framework import serializers

# serializers are used to define API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']