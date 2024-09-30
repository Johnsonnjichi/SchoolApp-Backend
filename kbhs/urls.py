from django.urls import path
from . import views


urlpatterns = [
# ContactUS Paths
path('', views.Home),
path('contactus/', views.Contact_us),
path('create/contact/', views.Create_Contact),
path('update/contact/<int:id>', views.Update_Contact),
path('delete/contact/<int:id>', views.Delete_Contact),

# AdmissionsForm Paths
path('admission/form', views.Get_AdmissionForm),
path('create/admission/', views.Create_AdmissionForm),
path('update/admission/<int:id>', views.Update_AdmissionForm),  



]