from rest_framework import authentication, permissions, viewsets

from .models import Dinosaur
from .serializers import DinosaurSerializer


class DefaultsMixin(object):

    # authentication_classes = (
    #     authentication.BasicAuthentication,
    #     authentication.TokenAuthentication,
    # )
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class DinosaurViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Dinosaur.objects.order_by("name")
    serializer_class = DinosaurSerializer
