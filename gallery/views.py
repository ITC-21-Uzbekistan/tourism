import base64

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import GetImageSerializer

from PIL import Image
from io import BytesIO


@api_view(['GET'])
def get_images(request):
    return Response("OK: GET")


@api_view(['GET'])
def get_detail_image(request, pk=0):
    return Response("OK: {}".format(pk))


@api_view(['POST'])
def create_image(request):
    # print(request.data)
    # print(request.FILES.get('image'))
    # if 'image' in request.data:
    #     img = Image.open(request.data.get('image'))
    #
    #     buffered = BytesIO()
    #     img.save(buffered, format='PNG')
    #     img_str = base64.b64encode(buffered.getvalue())

    return Response("Ok: POST")


@api_view(['PUT'])
def update_image(request):
    return Response("Ok: PUT")


@api_view(['DELETE'])
def delete_image(request):
    return Response("Ok: DELETE")
