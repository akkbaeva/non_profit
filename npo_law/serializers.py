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

