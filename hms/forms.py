from django import forms
from .models import Patient, Doctor, Appointment, Nurse, MedicalRecord, Billing


#Login form
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

#Registration form

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

        
#Creating Patients

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
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            #'blood_group': forms.Select(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')]),
        }



        def __init__(self, *args, **kwargs):
            super(PatientForm, self).__init__(*args, **kwargs)
            self.fields['national_id'].required = False


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
            'specialization': 'SPECIALIZATION',
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
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
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
    def __init__(self, *args, **kwargs):
        super(MedicalRecordForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].required = False
        self.fields['symptoms'].required = False
        self.fields['treatment'].required = False
        self.fields['prescription'].required = False
        self.fields['lab_results'].required = False
        self.fields['notes'].required = False
        
    
        

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
            'due_date': 'DUE DATE',
            'payment_status': 'PAYMENT STATUS',
            'payment_method': 'PAYMENT METHOD',
            'mpesa_transaction_code': 'MPESA CODE',
            'mpesa_transaction_date': 'MPESA DATE',
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_status': forms.Select(choices=[('Paid', 'Paid', 'U'), ('Pending', 'Pending')]),
            'mpesa_transaction_date': forms.DateInput(attrs={'type': 'date'}),
        }