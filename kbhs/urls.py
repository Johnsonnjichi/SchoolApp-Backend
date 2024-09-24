from django.urls import path
from . import views


urlpatterns = [
# ContactUS Paths
path('', views.Home),
path('contactus/', views.Contact_us),
path('create_contact/', views.Create_Contact),
path('update_contact/<int:id>', views.Update_Contact),
path('delete_contact/<int:id>', views.Delete_Contact),

# AdmissionsForm Paths




]