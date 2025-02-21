from django.urls import path, include
from . import views

urlpatterns = [ 
    path("", views.home, name="home"),
    path("patient", views.patient, name="patient_add"),
    path("doctor", views.doctor, name="doctor_add"),
    path("nurse", views.nurse, name="nurse_add"),
    path("appointment", views.appointment, name="appointment_add"),
    path("medical", views.medical, name="medical_add"),
    path("bill", views.bill, name="bill_add"),
    

]