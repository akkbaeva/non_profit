from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_publication.models import Publication
from npo_publication.serializers import PublicationSerializer, PublicationFavoriteSerializer, \
    PublicationFilterSearchSerializer


class PublicationAPIView(APIView, PageNumberPagination):
    allow_methods = ['GET', 'POST']
    serializer_class = PublicationSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        pub = Publication.objects.filter(Q(title__icontains=query) |
                                         Q(description__icontains=query))
        results = self.paginate_queryset(pub,
                                         request,
                                         view=self)
        return self.get_paginated_response(self.serializer_class(results,
                                                                 many=True,
                                                                 context={'request': request}).data)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        created_date = request.data.get('created_date')
        file = request.data.get('file')
        pub = Publication.objects.create(title=title,
                                         description=description,
                                         created_date=created_date,
                                         file=file)

        pub.save()
        return Response(data=self.serializer_class(pub).data,
                        status=status.HTTP_200_OK)


class PublicationDetailAPIView(APIView):
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PublicationSerializer

    def get(self, request, id):
        pub = Publication.objects.get(id=id)
        return Response(data=self.serializer_class(pub).data)

    def put(self, request, id):
        pub = Publication.objects.get(id=id)
        title = request.data.get('title')
        description = request.data.get('description')
        created_date = request.data.get('created_date')
        file = request.data.get('file')
        pub.title = title
        pub.description = description
        pub.file = file

        pub.save()
        return Response(data=self.serializer_class(pub).data,
                        status=status.HTTP_200_OK)

    def delete(self, request, id):
        pub = Publication.objects.get(id=id)
        pub.delete()

        return Response(data=self.serializer_class(pub).data,
                        status=status.HTTP_202_ACCEPTED)


class PublicationFavoriteAPIView(APIView):
    allow_methods = ['GET', 'POST', 'DELETE']
    serializers_class = PublicationSerializer

    def get(self, request):
        checkbox = Publication.objects.filter(user=request.user)
        return Response(data=PublicationFavoriteSerializer(checkbox).data)

    def post(self, request):
        pub_id = int(request.data.get('pub_id'))
        checkbox = Publication.objects.get(pub_id=pub_id,
                                           user=request.user)
        checkbox.save()
        return Response(data=PublicationFavoriteSerializer(checkbox).data,
                        status=status.HTTP_201_CREATED)

    def delete(self, request):
        pub_id = int(request.data.get('pub_id'))
        checkbox = Publication.objects.get(pub_id=pub_id,
                                           user_id=request.user)
        checkbox.delete()
        return Response(data=PublicationFavoriteSerializer(checkbox).data,
                        status=status.HTTP_204_NO_CONTENT)


class PublicationFilterSearchView(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationFilterSearchSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'description']
    search_fields = ['title', 'description']
    ordering_fields = ['title']
    ordering = ['title']