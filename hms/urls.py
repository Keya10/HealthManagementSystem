from django.urls import path, include
from . import views

urlpatterns = [ 
    path("", views.home, name="home"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("patient", views.patient, name="patient_add"),
    path("patient/list", views.patient_list, name="patient_list"),
    path("patient/update/<int:id>", views.patient_update, name="patient_update"),
    path("patient/delete/<int:id>", views.delete_patient, name="delete_patient"),
    
    path("doctor", views.doctor, name="doctor_add"),
    path("doctor/list", views.patient_list, name="doctor_list"),
    path("nurse", views.nurse, name="nurse_add"),
    path("nurse/list", views.patient_list, name="nurse_list"),
    path("appointment", views.appointment, name="appointment_add"),
    path("appointment/list", views.patient_list, name="appointment_list"),
    path("medical", views.medical, name="medical_add"),
    path("medical/list", views.medical_list, name="medical_list"),
    path("bill", views.bill, name="bill_add"),
    path("bill/list", views.bill_list, name="bill_list"),
    

]