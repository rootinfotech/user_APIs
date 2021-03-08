from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from . serializers import UserSerializer
from django.contrib.auth.models import User
# Create your views here.

class UserView(viewsets.ModelViewSet):
    """" user should be authenticated to perform write operation
        and anonymous user can only read data
        search, filter and ordering of user with username field"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['username']
    filterset_fields = ['username']
