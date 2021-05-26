from rest_framework import serializers
from npo_news.models import News, NewsFavorite
from npo_user.serializers import NPOUserSerializer


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id',
                  'title',
                  'description',
                  'created_date',
                  'image',
                  'link')


class NewsFavoriteSerializer(serializers.ModelSerializer):
    user = NPOUserSerializer()
    news = NewsSerializer()

    class Meta:
        model = NewsFavorite
        fields = 'id user news'
