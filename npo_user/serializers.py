from rest_framework import serializers
from npo_user.models import NPOUser


class NPOUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPOUser
        fields = ('id',
                  'username',
                  'email')
