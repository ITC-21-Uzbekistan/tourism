from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_images(request):
    return Response("OK: GET")


@api_view(['GET'])
def get_detail_image(request, pk=0):
    return Response("OK: {}".format(pk))


@api_view(['POST'])
def create_image(request):
    return Response("Ok: POST")


@api_view(['PUT'])
def update_image(request):
    return Response("Ok: PUT")


@api_view(['DELETE'])
def delete_image(request):
    return Response("Ok: DELETE")
