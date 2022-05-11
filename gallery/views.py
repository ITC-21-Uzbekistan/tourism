from rest_framework.decorators import api_view
from rest_framework.response import Response
from own_packages.CommonResult import CommonResult, CommonMessageResult
from .serializers import ImageSerializer
from relation.models import PrimaryKeysOfImages

import base64
from PIL import Image
from . import models
from io import BytesIO


@api_view(['GET'])
def get_images(request):
    result = CommonResult()

    try:
        data = list(models.Image.objects.all().values())
    except Exception as ex:
        print(ex)
    else:
        result.set_true(data)
    finally:
        return Response(result.__dict__)


@api_view(['GET'])
def get_detail_image(request, pk):
    result = CommonResult()

    try:
        obj = models.Image.objects.get(id=pk)
    except Exception as ex:
        print(ex)
    else:
        serializer = ImageSerializer(obj)

        if not serializer.is_valid():
            print(serializer.errors)
        else:
            result.set_true(serializer.data)
    finally:
        return Response(result.__dict__)


@api_view(['POST'])
def create_image(request):
    result = CommonMessageResult()
    if 'image' in request.data and request.data.get('image') is not None and 'type' in request.data \
            and request.data.get('type') is not None:
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
            # ---------------------------------
            PrimaryKeysOfImages.objects.create(
                primaykeyofimage=obj_image.id
            )
            # ---------------------------------
        except Exception as exept:
            print(exept)
        else:
            result.set_true()
        finally:
            return Response(result.__dict__)


@api_view(['PUT'])
def update_image(request, pk):
    result = CommonResult()

    try:
        obj = models.Image.objects.get(id=pk)
    except Exception as ex:
        print(ex)
    else:
        if 'image' in request.data and request.data.get('image') is not None and 'type' in request.data \
                and request.data.get('type') is not None:
            img = Image.open(request.data.get('image'))

            buffered = BytesIO()
            img.save(buffered, format='PNG')
            img_str = base64.b64encode(buffered.getvalue())

            obj.country = str(request.data.get('country'))
            obj.region = str(request.data.get('region'))
            obj.shrine = str(request.data.get('shrine'))
            obj.tour = str(request.data.get('tour'))
            obj.type = str(request.data.get('type'))
            obj.name = str(request.data.get('image'))
            obj.image = str(img_str)
            obj.altText = str(request.data.get('altText'))
            obj.description = str(request.data.get('description'))

            try:
                obj.save()
            except Exception as ex:
                print(ex)
            else:
                serializer = ImageSerializer(obj)

                if not serializer.is_valid():
                    print(serializer.errors)
                else:
                    result.set_true(serializer.data)
    finally:
        return Response(result.__dict__)


@api_view(['DELETE'])
def delete_image(request, pk):
    result = CommonMessageResult()
    try:
        data = models.Image.objects.get(id=pk)
        # --------------------------------------------------------------------------
        primarykey = PrimaryKeysOfImages.objects.get(primaykeyofimage=int(data.id))
        # --------------------------------------------------------------------------
    except Exception as ex:
        print(ex)
    else:
        try:
            # -----------------
            primarykey.delete()
            # -----------------
            data.delete()
        except Exception as ex:
            print(ex)
        else:
            result.set_true()
        finally:
            return Response(result.__dict__)
