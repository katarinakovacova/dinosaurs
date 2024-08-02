from rest_framework import authentication, permissions, viewsets

from .models import Dinosaur, User
from .permissions import IsOwner
from .serializers import DinosaurSerializer, UserSerializer


class DefaultsMixin(object):
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class DinosaurViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Dinosaur.objects.order_by("name")
    serializer_class = DinosaurSerializer


class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = User.objects.order_by("username")
    serializer_class = UserSerializer

    authentication_classes = (
        authentication.BasicAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner
    )


# TODO: /api/users/ should be read only and only show stuff for the current user (its ID)
