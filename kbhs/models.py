from django.db import models
from django.core.validators import EmailValidator
# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, validators=[EmailValidator()])
    message = models.TextField()

    def __str__(self):
        return self.name + '|' + self.message
    
class AdmissionForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fieldName1 = models.CharField()
    fieldName2 = models.CharField()
    fieldName3 = models.CharField()
    fieldName4 = models.CharField()
    fieldName5 = models.CharField()
    fieldName6 = models.CharField()
    fieldName7 = models.CharField()
    fieldName8 = models.CharField()
    fieldName9 = models.CharField()

    def __str__(self):
        return self.first_name + '|' + self.last_name
    
    
    