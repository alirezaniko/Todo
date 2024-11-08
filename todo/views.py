from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer, UserSerializer

from rest_framework import generics, mixins
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination

User = get_user_model()


# region generics
class TodosGenericsApiViewPagination(PageNumberPagination):
    page_size = 4


class TodosGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = TodosGenericsApiViewPagination


class TodoGenericsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
# endregion


class UserGenericsApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
