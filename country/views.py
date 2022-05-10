from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_countries(request, pk=0):
    if pk == 0:
        return HttpResponse("Get all countries")
    else:
        return HttpResponse("Get detail {}".format(pk))


@api_view(['POST'])
def create_country(request):
    return HttpResponse("Create")


@api_view(['PUT'])
def update_country(request, pk):
    return HttpResponse("Update {}".format(pk))


@api_view(['DELETE'])
def delete_country(request, pk):
    return HttpResponse("Delete {}".format(pk))
