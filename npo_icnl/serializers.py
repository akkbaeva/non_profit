from rest_framework import serializers

from npo_icnl.models import ICNL
from npo_user.serializers import NPOUserSerializer


class ICNLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICNL
        fields = ('id', 'title', 'description',
                  'created_date', 'file')


class ICNLFavoriteSerializer(serializers.ModelSerializer):
    user = NPOUserSerializer()
    icnl = ICNLSerializer()

    class Meta:
        model = ICNL
        fields = 'id user icnl'.split()