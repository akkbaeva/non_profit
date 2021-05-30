from rest_framework import serializers
from npo_publication.models import Publication, PublicationFavorite
from npo_user.serializers import NPOUserSerializer


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id',
                  'title',
                  'description',
                  'created_date',
                  'file')


class PublicationFavoriteSerializer(serializers.ModelSerializer):
    user = NPOUserSerializer
    pub = PublicationSerializer

    class Meta:
        model = PublicationFavorite
        fields = 'id user pub'


class PublicationFilterSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('title', 'description')
