from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
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

@api_view(['POST'])
def Create_Contact(request):
    serializer = ContactUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('message:Created successfully', status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def Update_Contact(request, id):
    contact = ContactUs.objects.get(id=id)
    serializer = ContactUsSerializer(contact, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response('message:Updated successfully', status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def Delete_Contact(request, id):
    contact = get_object_or_404(ContactUs, id=id)
    # contact = ContactUs.objects.get(id=id)
    contact.delete()
    return Response('message:Deleted successfully', status=status.HTTP_200_OK)
    





