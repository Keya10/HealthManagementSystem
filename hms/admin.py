from django.contrib import admin
from .models import Patient, Doctor
# Register your models here.

@admin.register(Patient, Doctor)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'first_name', 'last_name', 'national_id', 'gender')
    search_fields = ('national_id', 'first_name', 'last_name', 'national_id')
    list_filter = 'gender', 'blood_group'

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'phone_number')
    search_fields = ('first_name', 'last_name', 'license_number', 'specialization')
    list_filter = ('specialization', 'department')