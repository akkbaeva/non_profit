from rest_framework import serializers
from npo_news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id',
                  'title',
                  'description',
                  'created_date',
                  'image',
                  'link')
