from django.db.models import Q

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_law.models import NPOLaw, LawFavorite
from npo_law.serializers import NPOLawSerializer, LawFilterSearchSerializer


class NPOLawAPIView(APIView, PageNumberPagination):
    allow_methods = ['GET', 'POST']
    serializer_class = NPOLawSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        law = NPOLaw.objects.filter(Q(title__icontains=query) |
                                    Q(description__icontains=query))
        results = self.paginate_queryset(law,
                                         request,
                                         view=self)
        return self.get_paginated_response(self.serializer_class(results,
                                                                 many=True,
                                                                 context={'request': request}).data)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        created_date = request.data.get('created date')
        file = request.data.get('file')
        law = NPOLaw.objects.create(title=title,
                                    description=description,
                                    created_date=created_date,
                                    file=file)
        law.save()
        return Response(data=self.serializer_class(law).data,
                        status=status.HTTP_201_CREATED)


class NPOLawDetailAPIView(APIView):
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = NPOLawSerializer

    def get(self, request, id):
        law = NPOLaw.objects.get(id=id)
        return Response(data=self.serializer_class(law).data,
                        status=status.HTTP_200_OK)

    def put(self, request, id):
        law = NPOLaw.objects.get(id=id)
        title = request.data.get('title')
        description = request.data.get('description')
        file = request.data.get('file')
        law.title = title
        law.description = description
        law.file = file

        return Response(data=self.serializer_class(law).data,
                        status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        law = NPOLaw.objects.get(id=id)
        law.delete()
        return Response(data=self.serializer_class(law).data,
                        status=status.HTTP_200_OK)


class LawFavoriteAPIView(APIView):
    allow_methods = ['GET', 'POST', 'DELETE']
    serializer_class = NPOLawSerializer

    def get(self, request):
        favorite = LawFavorite.objects.filter(user=request.user)
        return Response(data=NPOLawSerializer(favorite).data)

    def post(self, request):
        law_id = int(request.data.get('law_id'))
        favorite = LawFavorite.objects.get(law_id=law_id,
                                           user=request.user)
        favorite.save()
        return Response(data=NPOLawSerializer(favorite).data,
                        status=status.HTTP_201_CREATED)

    def delete(self, request):
        law_id = int(request.data.get('law_id'))
        favorite = LawFavorite.objects.get(law_id=law_id,
                                           user=request.user)
        favorite.save()
        return Response(data=NPOLawSerializer(favorite).data,
                        status=status.HTTP_204_NO_CONTENT)


class LawFilterSearchView(viewsets.ModelViewSet):
    queryset = NPOLaw.objects.all()
    serializer_class = LawFilterSearchSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'description']
    search_fields = ['=title', '=description']
