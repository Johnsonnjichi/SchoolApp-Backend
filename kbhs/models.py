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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    is_boarder = models.BooleanField(default=False) # True for boarders, False for day scholars
    dormitory = models.CharField(max_length=100)



    def __str__(self):
        return self.first_name + '|' + self.last_name
    

    
    