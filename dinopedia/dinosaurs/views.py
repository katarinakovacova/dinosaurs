from rest_framework import authentication, permissions, viewsets, mixins

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


class UserViewSet(mixins.RetrieveModelMixin, 
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"

    authentication_classes = (
        authentication.BasicAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner
    )
