from django.contrib import admin
from .models import Patient, Doctor, Appointment, Nurse, MedicalRecord, Billing, Department, Specialization

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'first_name', 'last_name', 'gender', 'blood_group')
    search_fields = ('national_id', 'first_name', 'last_name')
    list_filter = ('gender', 'blood_group')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'phone_number')
    search_fields = ('first_name', 'last_name', 'license_number', 'specialization')
    list_filter = ('specialization', 'department')

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'license_number', 'phone_number', 'department')
    search_fields = ('first_name', 'last_name', 'license_number')
    list_filter = ('department',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'nurse', 'date', 'time', 'status')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name')
    list_filter = ('status', 'date', 'doctor')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'diagnosis', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'diagnosis')
    list_filter = ('created_at', 'doctor')

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('bill_number', 'patient', 'amount', 'payment_status', 'payment_method', 'date_issued')
    search_fields = ('bill_number', 'patient__first_name', 'patient__last_name')
    list_filter = ('payment_status', 'payment_method', 'date_issued')