from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [ 
    path("", views.home, name="home"),
    path("", views.dashboard, name="dashboard"),
    path("patient", views.patient, name="patient_add"),
    path("patient/list", views.patient_list, name="patient_list"),
    path("patient/update/<int:id>", views.patient_update, name="patient_update"),
    path("patient/delete/<int:id>", views.delete_patient, name="delete_patient"),
    
    path("doctor", views.doctor, name="doctor_add"),
    path("doctor/list", views.doctor_list, name="doctor_list"),
    path("doctor/update/<int:id>", views.doctor_update, name="doctor_update"),
    path("doctor/delete/<int:id>", views.delete_doctor, name="delete_doctor"),


    path("nurse", views.nurse, name="nurse_add"),
    path("nurse/list", views.nurse_list, name="nurse_list"),
    path("nurse/update/<int:id>", views.nurse_update, name="nurse_update"),
    path("nurse/delete/<int:id>", views.delete_nurse, name="delete_nurse"),

   
    path("appointment", views.appointment, name="appointment_add"),
    path("appointment/list", views.appointment_list, name="appointment_list"),
    path("appointment/update/<int:id>", views.appointment_update, name="appointment_update"),
    path("appointment/delete/<int:id>", views.delete_appointment, name="delete_appointment"),



    path("medical", views.medical, name="medical_add"),
    path("medical/list", views.medical_list, name="medical_list"),
    path("medical/update/<int:id>", views.medical_update, name="medical_update"),
    path("medical/delete/<int:id>", views.delete_medical, name="delete_medical"),



    path("bill", views.bill, name="bill_add"),
    path("bill/list", views.bill_list, name="bill_list"),
    path("nurse/update/<int:id>", views.nurse_update, name="nurse_update"),
    path("nurse/delete/<int:id>", views.delete_nurse, name="delete_nurse"),

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)