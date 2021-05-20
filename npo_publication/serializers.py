from rest_framework import serializers
from npo_publication.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id',
                  'title',
                  'description',
                  'created_date',
                  'file')

