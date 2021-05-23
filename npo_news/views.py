from django.db.models import Q
from rest_framework import status

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_news.models import News, NewsFavorite
from npo_news.serializers import NewsSerializer, NewsFavoriteSerializer


class NewAPIView(APIView, PageNumberPagination):
    allow_methods = ['GET', 'POST']
    serializer_class = NewsSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        news = News.objects.filter(Q(title__icontains=query) |
                                   Q(description__icontains=query))
        results = self.paginate_queryset(news,
                                         request,
                                         view=self)
        return self.get_paginated_response(self.serializer_class(results,
                                                                 many=True,
                                                                 context={'request': request}).data)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        image = request.data.get('image')
        link = request.data.get('link')
        news = News.objects.create(title=title,
                                   description=description,
                                   image=image,
                                   link=link)
        news.save()
        return Response(data=self.serializer_class(news).data,
                        status=status.HTTP_201_CREATED)


class NewDetailAPIView(APIView):
    allow_method = ['GET', 'PUT', 'DELETE']
    serializer_class = NewsSerializer

    def get(self, request, id, *args, **kwargs):
        news = News.objects.get(id=id)
        return Response(data=self.serializer_class(news).data)

    def put(self, request, id, *args, **kwargs):
        news = News.objects.get(id=id)
        title = request.data.get('title')
        description = request.data.get('description')
        image = request.data.get('image')
        link = request.data.get('link')
        news.title = title
        news.description = description
        news.image = image
        news.link = link

        news.save()
        return Response(data=self.serializer_class(news).data,
                        status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        news = News.objects.get(id=id)
        news.delete()

        return Response(status=status.HTTP_202_ACCEPTED)


class NewFavoriteAPIView(APIView):
    allow_methods = ['GET', 'POST', 'DELETE']
    serializer_class = NewsFavoriteSerializer

    def get(self, request):
        saved = NewsFavorite.objects.filter(user=request.user)
        return Response(data=NewsFavoriteSerializer(saved).data,
                        status=status.HTTP_200_OK)

    def post(self, request):
        news_id = int(request.data.get('news_id'))
        saved = NewsFavorite.objects.get(news_id=news_id,
                                         user=request.user)
        saved.save()
        return Response(data=NewsFavoriteSerializer(saved).data,
                        status=status.HTTP_201_CREATED)

    def delete(self, request):
        news_id = int(request.data.get('news_id'))
        saved = NewsFavorite.objects.get(news_id=news_id,
                                         user_id=request.user)
        saved.delete()
        return Response(data=NewsFavoriteSerializer(saved).data,
                        status=status.HTTP_204_NO_CONTENT)
