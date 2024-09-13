from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import *
from . models import *

# Create your views here.
@api_view(['GET'])
def Home(request):
    print('johnson')
    return Response({'Hello World!'})

@api_view(['GET'])
def Contact_us(request):
    contact = ContactUs.objects.all()
    serializer = ContactUsSerializer(contact, many=True)
    return Response(serializer.data)

