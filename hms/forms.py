from django import forms
from .models import Patient, Doctor, Appointment, Nurse, MedicalRecord, Billing


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields ='first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email', 'address', 'blood_group', 'medical_history', 'emergency_contact_name', 'emergency_contact_phone'
        lables = {
            'national_id': 'NATIONAL ID',
            'first_name': 'FIRST NAME',
            'last_name': 'LAST NAME',
            'date_of_birth': 'DATE OF BIRTH',
            'gender':   'GENDER',
            'phone_number': 'PHONE NUMBER',
            'email': 'EMAIL',
            'address': 'ADDRESS',
            'blood_group': 'BLOOD GROUP',
            'medical_history': 'MEDICAL HISTORY',
            'emergency_contact_name': 'EMERGENCY CONTACT NAME',
            'emergency_contact_phone': 'EMERGENCY CONTACT PHONE',

        }

        national_id = forms.CharField(max_length=10, required=False)
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        lables = {
            'national_id': 'NATIONAL ID',
            'first_name': 'FIRST NAME',
            'last_name': 'LAST NAME',
            'date_of_birth': 'DATE OF BIRTH',
            'gender':   'GENDER',
            'phone_number': 'PHONE NUMBER',
            'email': 'EMAIL',
            'address': 'ADDRESS',
            'specialization': 'SPECIALIZATION',
            'license_number': 'LICENSE NUMBER',
            'years_of_experience': 'YEARS OF EXPERIENCE',
            'department': 'DEPARTMENT',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'
        lables = {
            'first_name': 'FIRST NAME',
            'last_name': 'LAST NAME',
            'date_of_birth': 'DATE OF BIRTH',
            'gender':   'GENDER',
            'license_number': 'LICENSE NUMBER',
            'years_of_experience': 'YEARS OF EXPERIENCE',
            'phone_number': 'PHONE NUMBER',
            'email': 'EMAIL',
            'address': 'ADDRESS',
            'department': 'DEPARTMENT',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        lables = {
            'patient': 'PATIENT',
            'doctor': 'DOCTOR',
            'nurse': 'NURSE',
            'date': 'DATE',
            'time': 'TIME',
            'status': 'STATUS',
        }

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        lables = {
            'patient': 'PATIENT',
            'doctor': 'DOCTOR',
            'diagnosis': 'DIAGNOSIS',
            'symptoms': 'SYMPTOMS',
            'treatment': 'TREATMENT',
            'prescription': 'PRESCRIPTION',
            'lab_results': 'LAB RESULTS',
            'notes': 'NOTES',
        }

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'
        lables = {
            'patient': 'PATIENT',
            'appointment': 'APPOINTMENT',
            'bill_number': 'BILL NUMBER',
            'description': 'DESCRIPTION',
            'amount': 'AMOUNT',
            'payment_status': 'PAYMENT STATUS',
            'payment_method': 'PAYMENT METHOD',
            'mpesa_transaction_code': 'MPESA CODE',
            'mpesa_transaction_date': 'MPESA DATE',
        }