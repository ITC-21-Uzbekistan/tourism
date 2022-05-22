from rest_framework.decorators import api_view
from rest_framework.response import Response

from own_packages.CommonResult import CommonResult, CommonMessageResult
from own_packages.clear_string import clear_string
from .models import Country,ContentCountry
from relation.models import PrimaryKeysOfImages
from .serializers import CountrySerializer


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
