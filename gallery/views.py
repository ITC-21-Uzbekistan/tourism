from rest_framework.decorators import api_view
from rest_framework.response import Response

import base64
from PIL import Image
from . import models
from io import BytesIO


@api_view(['GET'])
def get_images(request):
    return Response("OK: GET")


@api_view(['GET'])
def get_detail_image(request, pk=0):
    return Response("OK: {}".format(pk))


@api_view(['POST'])
def create_image(request):
    print(request.data)
    if 'image' in request.data and request.data.get('image') is not None and 'type' in request.data and request.data.get('type') is not None:
        img = Image.open(request.data.get('image'))

        buffered = BytesIO()
        img.save(buffered, format='PNG')
        img_str = base64.b64encode(buffered.getvalue())

        obj_image = models.Image.objects.create(
            country=str(request.data.get('country')),
            region=str(request.data.get('region')),
            shrine=str(request.data.get('shrine')),
            tour=str(request.data.get('tour')),
            type=str(request.data.get('type')),
            name=str(request.data.get('image')),
            image=str(img_str),
            altText=str(request.data.get('altText')),
            description=str(request.data.get('description'))
        )
        try:
            obj_image.save()
            return Response("Ok: POST")
        except Exception as exept:
            print(exept)
            return Response("No no no")


@api_view(['PUT'])
def update_image(request):
    return Response("Ok: PUT")


@api_view(['DELETE'])
def delete_image(request):
    return Response("Ok: DELETE")
