from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TypeImage
from .serializers import TypeImageSerializer
from own_packages.CommonResult import CommonResult, CommonMessageResult


@api_view(['GET'])
def get_types(request):
    result = CommonResult()
    try:
        data = list(TypeImage.objects.all().values())
    except Exception as ex:
        print(ex)
    else:
        result.set_true(data)
    return Response(result.__dict__)


@api_view(['GET'])
def get_detail_types(request, pk):
    result = CommonResult()
    try:
        obj = TypeImage.objects.get(id=pk)
    except Exception as ex:
        print(ex)
    else:
        data = TypeImageSerializer(obj).data
        result.set_true(data)
    return Response(result.__dict__)


@api_view(['POST'])
def create_type(request):
    result = CommonMessageResult()
    serializer = TypeImageSerializer(data=request.data)

    if not serializer.is_valid():
        print(serializer.errors)
    else:
        serializer.save()
        result.set_true()

    return Response(result.__dict__)


@api_view(['PUT'])
def update_type(request, pk):
    result = CommonResult()
    data = TypeImage.objects.get(id=pk)
    serializer = TypeImageSerializer(instance=data, data=request.data)

    if not serializer.is_valid():
        print(serializer.errors)
    else:
        serializer.save()
        result.set_true(serializer.data)

    return Response(result.__dict__)


@api_view(['DELETE'])
def delete_type(request, pk):
    result = CommonMessageResult()

    try:
        data = TypeImage.objects.get(id=pk)
    except Exception as ex:
        print(ex)
    else:
        data.delete()
        result.set_true()

    return Response(result.__dict__)
