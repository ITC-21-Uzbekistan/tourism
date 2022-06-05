from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED,
                                   HTTP_501_NOT_IMPLEMENTED, HTTP_204_NO_CONTENT,)

from country.pagination import CountryPagination
from .models import Lang, Content, Country
from .serializers import ContentSerializer, CountrySerializer, LangSerializer, CountryCreateSerializer


class CountryCreateView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryCreateSerializer

    # def list(self, request, *args, **kwargs):
    #     try:
    #         lang = Lang.objects.get(short=request.headers['lang'])
    #     except Exception as ex:
    #         print(ex)
    #         return Response({'message': 'This language does not exist'}, status=HTTP_404_NOT_FOUND)
    #     else:
    #         queryset = self.get_queryset()
    #
    #         serializer = CountrySerializer(queryset, many=True, context={'lang': str(lang.short)})
    #
    #         return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        return Response({"massage": "success"}, status=status.HTTP_201_CREATED)


class CountryListView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    pagination_class = CountryPagination
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        lang = request.headers['lang']
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(lang__short__icontains=lang)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary="Davlatlar ro'yhatini ko'rish tillar bilan", )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RetrieveUpdateDestroyCountry(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            lang = Lang.objects.get(short=request.headers['lang'])
        except Exception as ex:
            print(ex)
            return Response({'message': 'This language does not exist'}, status=HTTP_404_NOT_FOUND)
        else:
            country = self.get_object()
            serializer = CountrySerializer(country, context={'lang': lang.short})
            return Response(serializer.data, status=HTTP_200_OK)

    # def partial_update(self, request, *args, **kwargs):
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass

    def destroy(self, request, *args, **kwargs):
        country = self.get_object()
        country.delete()

        return Response(status=HTTP_204_NO_CONTENT)