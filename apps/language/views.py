from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from rest_framework.generics import (GenericAPIView, CreateAPIView, ListCreateAPIView,
                                     DestroyAPIView, UpdateAPIView, RetrieveAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.parsers import MultiPartParser, JSONParser
# from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
# from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Language
from .pagination import LanguagePagination
from .serializers import LanguageSerializers


class ListCreateLanguageView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers
    pagination_class = LanguagePagination
    filter_backends = (filters.SearchFilter,)
    # permission_classes = [IsAdminUser, ]
    # authentication_classes = [JWTAuthentication, ]
    parser_classes = [JSONParser, ]

    @swagger_auto_schema(operation_summary="Tillar ro'yhatini ko'rish", )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(operation_summary="Yangi til kiritish",)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateDestroyLanguageView(GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers
    pagination_class = LanguagePagination
    filter_backends = (filters.SearchFilter,)
    # permission_classes = [IsAdminUser, ]
    # authentication_classes = [JWTAuthentication, ]
    parser_classes = [MultiPartParser, ]

    @swagger_auto_schema(operation_summary="Til haqidagi ma`lumotlarni yangilash", )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Til haqidagi ma`lumotlarni qisman yangilash", )
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
