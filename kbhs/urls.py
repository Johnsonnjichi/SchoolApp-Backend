from django.urls import path
from . import views


urlpatterns = [

path('', views.Home),
path('contactus/', views.Contact_us),
]