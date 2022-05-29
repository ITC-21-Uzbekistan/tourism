from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import (GenericAPIView, ListAPIView, CreateAPIView,
                                     DestroyAPIView, RetrieveAPIView, UpdateAPIView, ListCreateAPIView)
from rest_framework_simplejwt.authentication import JWTAuthentication

from .pagination import CountryPagination
from own_packages.CommonResult import CommonResult, CommonMessageResult
from own_packages.clear_string import clear_string
from .models import Country, ContentCountry
from relation.models import PrimaryKeysOfImages
from .serializers import CountrySerializer, ContentCountrySerializer


@api_view(['GET'])
def get_countries(request):
    lang = request.params.lang
    result = CommonResult()
    try:
        countries = list(Country.objects.all().values())
    except Exception as ex:
        print(ex)
    else:
        data = []
        for country in countries:
            # I have stopped here
            content = ContentCountry.objects.get(country=country, language=lang)
            data.append({
                "country_name": ContentCountry.objects.get(country)
            })
        result.set_true(data)
    finally:
        return Response(result.__dict__)


@api_view(['GET'])
def get_detail_country(request, pk):
    result = CommonResult()

    try:
        data = Country.objects.get(id=pk)
    except Exception as ex:
        print(ex)
    else:
        serializer = CountrySerializer(data)

        if not serializer.is_valid():
            print(serializer.errors)
        else:
            result.set_true(serializer.data)
    finally:
        return Response(result.__dict__)


@api_view(['POST'])
def create_country(request):
    result = CommonMessageResult()

    data = Country.objects.create(
        name=request.data.get('name'),
        info=request.data.get('info'),
        url=clear_string(request.data.get('name')),
        location=request.data.get('location')
    )

    for i in request.data.get('images'):
        data.images.add(PrimaryKeysOfImages.objects.get(primaykeyofimage=i))

    try:
        data.save()
    except Exception as ex:
        print(ex)
    else:
        result.set_true()
    finally:
        return Response(result.__dict__)


@api_view(['PUT'])
def update_country(request, pk):
    result = CommonResult()

    try:
        obj = Country.objects.get(id=pk)
    except Exception as ex:
        print(ex)
    else:
        obj.name = request.data.get('name')
        obj.info = request.data.get('info')
        obj.url = request.data.get('url')
        obj.location = request.data.get('location')

        # for image in :

    return Response("Update {}".format(pk))


@api_view(['DELETE'])
def delete_country(request, pk):
    result = CommonMessageResult()
    try:
        data = Country.objects.get(id=pk)
    except Exception as ex:
        print(ex)
    else:
        try:
            data.delete()
        except Exception as ex:
            print(ex)
        else:
            result.set_true()
    finally:
        return Response(result.__dict__)


class ListCountryView(ListAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountrySerializer
    pagination_class = CountryPagination
    filter_backends = (filters.SearchFilter, )
    # permission_classes = [IsAdminUser, ]
    # authentication_classes = [JWTAuthentication, ]
    parser_classes = [JSONParser, ]

    @swagger_auto_schema(operation_summary="Davlatlar ro'yhatini ko'rish", )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateCountryView(CreateAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountrySerializer
    pagination_class = CountryPagination
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser, ]
    authentication_classes = [JWTAuthentication, ]
    parser_classes = [MultiPartParser, ]

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(operation_summary="Yangi Davlat kiritish",)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DeleteUpdateCountryView(GenericAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountrySerializer
    pagination_class = CountryPagination
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser, ]
    authentication_classes = [JWTAuthentication, ]
    parser_classes = [JSONParser, ]

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @swagger_auto_schema(operation_summary="Davlat ma'lumotlarini yangilash", )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Davlat ma'lumotlarini qisman yangilash", )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete = True
        instance.save()
        # instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(operation_summary="Davlat ma`lumotlarini o'chirish", )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RetrieveCountryView(GenericAPIView):
    queryset = ContentCountry.objects.all()
    serializer_class = ContentCountrySerializer
    filter_backends = (filters.SearchFilter, )
    parser_classes = [JSONParser, ]

    def retrieve(self, request, *args, **kwargs):
        # lang = request.get_full_path().split('/')[1]
        lang = 'uz'
        instance = self.queryset.filter(language__language_short__icontains=lang).\
            filter(country__country_name=kwargs.get("country", "uzbekistan")).first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary="Davlat haqidagi to'liq ma'lumotni ko'rish til bo'yicha", )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ListCreateContentCountryView(ListCreateAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = ContentCountrySerializer
    pagination_class = CountryPagination
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser, ]
    authentication_classes = [JWTAuthentication, ]
    parser_classes = [MultiPartParser, ]

    @swagger_auto_schema(operation_summary="Davlatlar ro'yhatini ko'rish tillar bilan", )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(operation_summary="Yangi Davlat kiritish tillar boyicha",)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

