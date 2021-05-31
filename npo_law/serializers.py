from rest_framework import serializers

from npo_law.models import NPOLaw


class NPOLawSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPOLaw
        fields = ('id',
                  'title',
                  'description',
                  'created_date',
                  'file')


class LawFavoriteSerializer(serializers.ModelSerializer):
    user = NPOLawSerializer
    law = NPOLawSerializer

    class Meta:
        model = NPOLaw
        fields = 'id user law'.split()


class LawFilterSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPOLaw
        fields = ('id', 'title', 'description')

