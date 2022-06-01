from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_501_NOT_IMPLEMENTED, HTTP_204_NO_CONTENT
from .models import Lang, Content, Country
from .serializers import ContentSerializer, CountrySerializer, LangSerializer


class CountryAPIView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self, request, *args, **kwargs):
        try:
            lang = Lang.objects.get(short=request.headers['lang'])
        except Exception as ex:
            print(ex)
            return Response({'message': 'This language does not exist'}, status=HTTP_404_NOT_FOUND)
        else:
            queryset = self.get_queryset()

            serializer = CountrySerializer(queryset, many=True, context={'lang': str(lang.short)})

            return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        try:
            country = Country.objects.create(name=request.data['country_name'])
        except Exception as ex:
            print(ex)
        else:
            contents = []
            for content in request.data['content']:
                try:
                    lang = Lang.objects.get(short=content['lang'])
                except Exception as ex:
                    print(ex)
                    continue
                else:
                    try:
                        ccc = Content.objects.create(
                            lang=lang,
                            country=country,
                            country_name=content['country_name'],
                            country_info=content['country_info']
                        )
                        contents.append(ccc)
                        ccc.save()
                    except Exception as ex:
                        print(ex)
                        country.delete()
                        for cont in contents:
                            cont.delete()
                        return Response({'message': 'Try again later'}, status=HTTP_501_NOT_IMPLEMENTED)

        return Response(status=HTTP_201_CREATED)


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

