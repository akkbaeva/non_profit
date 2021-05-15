from django.db.models import Q
from rest_framework import status

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_news.models import News
from npo_news.serializers import NewsSerializer


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
        created_date = request.data.get('created_date')
        image = request.data.get('image')
        link = request.data.get('link')

        news.save()
        return Response(data=self.serializer_class(news).data,
                        status=status.HTTP_201_CREATED)

    def delete(self, request, id, *args, **kwargs):
        news = News.objects.get(id=id)
        news.delete()

        return Response(status=status.HTTP_200_OK)
