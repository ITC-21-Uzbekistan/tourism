from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def main(request):
    return Response({
        'image_simpe': 'https://bekkitourism.herokuapp.com/media/images/8888.jpg'
    })