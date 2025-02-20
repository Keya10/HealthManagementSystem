from django.contrib import admin
from .models import Patient
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'first_name', 'last_name', 'national_id', 'gender')
    search_fields = ('national_id', 'first_name', 'last_name', 'national_id')
    list_filter = 'gender', 'blood_group'
    
