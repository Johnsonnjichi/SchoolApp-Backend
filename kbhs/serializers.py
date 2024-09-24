from rest_framework import serializers
from . models import *

class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = '__all__' 

class AdmissionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionForm
        fields = '__all__'

 