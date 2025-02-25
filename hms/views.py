from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from datetime import datetime, timedelta
from .forms import PatientForm, DoctorForm, NurseForm, AppointmentForm, MedicalRecordForm, BillingForm, RegistrationForm
from .models import Patient, Doctor, Nurse, Appointment, MedicalRecord, Billing


#login view
def login_view(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    
    return redirect(request,'registration/register.html', {'form' : form})

# Dashboard view
def dashboard(request):
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_nurses = Nurse.objects.count()
    total_appointments = Appointment.objects.count()
    total_revenue = Billing.objects.aggregate(total=Sum('amount'))['total'] or 0
    pending_bills = Billing.objects.filter(payment_status='Pending').count()

    patients_registration_data = []
    patients_registration_labels = []
    for i in range(6, -1, -1):
        date = datetime.today() - timedelta(days=i)
        count = Patient.objects.filter(created_at__date=date).count()
        patients_registration_data.append(count)
        patients_registration_labels.append(date.strftime('%a'))

    appointment_data = [10, 20, 30, 40, 50, 60, 70]  # Replace with actual data
    appointment_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']  # Replace with actual labels

    billing_labels = ['Paid', 'Pending']
    billing_data = [
        Billing.objects.filter(payment_status='Paid').count(),
        Billing.objects.filter(payment_status='Pending').count(),
    ]

    context = {
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'total_revenue': total_revenue,
        'pending_bills': pending_bills,
        'patients_registration_data': patients_registration_data,
        'patients_registration_labels': patients_registration_labels,
        'appointment_data': appointment_data,
        'appointment_labels': appointment_labels,
        'billing_labels': billing_labels,
        'billing_data': billing_data,
    }
    return render(request, 'dashboard.html', context)

def home(request):
    return render(request, 'home.html')

def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully')
            return redirect('patient_list')
        else:
            messages.error(request, 'Invalid data. Please check the form')
    else:
        form = PatientForm()
    return render(request, 'patient_add.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_update(request, id):
    patient = get_object_or_404(Patient, pk=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient updated successfully')
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient_update.html', {'form': form})

def delete_patient(request, id):
    patient = get_object_or_404(Patient, pk=id)
    patient.delete()
    messages.success(request, 'Patient deleted successfully')
    return redirect('patient_list')

def doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor added successfully')
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor_add.html', {'form': form})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_update(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor updated successfully')
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_update.html', {'form': form})

def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    doctor.delete()
    messages.success(request, 'Doctor deleted successfully')
    return redirect('doctor_list')

def nurse(request):
    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nurse added successfully')
            return redirect('nurse_list')
    else:
        form = NurseForm()
    return render(request, 'nurse_add.html', {'form': form})

def nurse_list(request):
    nurses = Nurse.objects.all()
    return render(request, 'nurse_list.html', {'nurses': nurses})

def nurse_update(request, id):
    nurse = get_object_or_404(Nurse, pk=id)
    if request.method == 'POST':
        form = NurseForm(request.POST, instance=nurse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nurse updated successfully')
            return redirect('nurse_list')
    else:
        form = NurseForm(instance=nurse)
    return render(request, 'nurse_update.html', {'form': form})

def delete_nurse(request, id):
    nurse = get_object_or_404(Nurse, pk=id)
    nurse.delete()
    messages.success(request, 'Nurse deleted successfully')
    return redirect('nurse_list')

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment booked successfully')
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_add.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

def appointment_update(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully')
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_update.html', {'form': form})

def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    appointment.delete()
    messages.success(request, 'Appointment deleted successfully')
    return redirect('appointment_list')

def medical(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medical record added successfully')
            return redirect('medical_list')
    else:
        form = MedicalRecordForm()
    return render(request, 'medical_add.html', {'form': form})

def medical_list(request):
    medical_records = MedicalRecord.objects.all()
    return render(request, 'medical_list.html', {'medical_records': medical_records})

def medical_update(request, id):
    medical_record = get_object_or_404(MedicalRecord, pk=id)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medical record updated successfully')
            return redirect('medical_list')
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'medical_update.html', {'form': form})

def delete_medical(request, id):
    medical_record = get_object_or_404(MedicalRecord, pk=id)
    medical_record.delete()
    messages.success(request, 'Medical record deleted successfully')
    return redirect('medical_list')

def bill(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bill added successfully')
            return redirect('bill_list')
    else:
        form = BillingForm()
    return render(request, 'bill_add.html', {'form': form})

def bill_list(request):
    bills = Billing.objects.all()
    return render(request, 'bill_list.html', {'bills': bills})