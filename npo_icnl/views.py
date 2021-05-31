from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_icnl.models import ICNL, ICNLFavorite
from npo_icnl.permissions import ISCLIENT
from npo_icnl.serializers import ICNLSerializer, ICNLFavoriteSerializer


class ICNLAPIView(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    serializer_class = ICNLSerializer
    queryset = ICNL.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)


class ICNLDetailAPIView(generics.GenericAPIView,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    serializer_class = ICNLSerializer
    queryset = ICNL.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, id=id)

    def put(self, request, *args, **kwargs):
        return self.update(request, id=id)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, id=id)


class ICNLFavoriteAPIView(APIView):
    allow_methods = ['GET', 'POST', 'DELETE']
    serializer_class = ICNLFavoriteSerializer
    permission_classes = [ISCLIENT]

    def get(self, request):
        saved = ICNLFavorite.objects.filter(user=request.user)
        return Response(data=ICNLFavoriteSerializer(saved).data)

    def post(self, request):
        icnl_id = int(request.data.get('icnl_id'))
        saved = ICNLFavorite.objects.create(icnl_id=icnl_id,
                                            user=request.user)

        saved.save()
        return Response(data=ICNLFavoriteSerializer(saved).data,
                        status=status.HTTP_201_CREATED)

    def delete(self, request):
        icnl_id = int(request.data.get('icnl_id'))
        saved = ICNLFavorite.objects.get(icnl_id=icnl_id,
                                         user=request.user)
        saved.delete()
        return Response(data=ICNLFavoriteSerializer(saved).data,
                        status=status.HTTP_204_NO_CONTENT)
