from django.contrib import admin
from .models import Patient, Doctor, Appointment,Nurse,MedicalRecord,Billing
# Register your models here.

@admin.register(Patient, Doctor, Appointment,Nurse,MedicalRecord,Billing)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'first_name', 'last_name', 'national_id', 'gender')
    search_fields = ('national_id', 'first_name', 'last_name', 'national_id')
    list_filter = 'gender', 'blood_group'

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'phone_number')
    search_fields = ('first_name', 'last_name', 'license_number', 'specialization')
    list_filter = ('specialization', 'department')

class NurseAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'qualification', 'hospital_name', 'phone_number')
    search_fields = ('first_name', 'last_name', 'license_number', 'qualification')
    list_filter = ('department', 'qualification')

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'diagnosis', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'diagnosis')
    list_filter = ('created_at', 'doctor')


class BillingAdmin(admin.ModelAdmin):
    list_display = ('bill_number', 'patient', 'amount', 'payment_status', 'payment_method', 'date_issued')
    search_fields = ('bill_number', 'patient__first_name', 'patient__last_name')
    list_filter = ('payment_status', 'payment_method', 'date_issued')