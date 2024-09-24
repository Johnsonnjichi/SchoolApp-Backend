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
    surname = models.CharField(max_length=30)
    admission_number = models.CharField(max_length=100)
    day_scholer = models.CharField(max_length=100)
    fieldName4 = models.CharField(max_length=100)
    fieldName5 = models.CharField(max_length=100)
    fieldName6 = models.CharField(max_length=100)
    fieldName7 = models.CharField(max_length=100)
    fieldName8 = models.CharField(max_length=100)
    fieldName9 = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + '|' + self.last_name
    
  
    
    