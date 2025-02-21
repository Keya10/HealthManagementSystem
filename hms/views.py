from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Sum, Count
from datetime import datetime, timedelta
from .forms import PatientForm, DoctorForm, NurseForm, AppointmentForm, MedicalRecordForm, BillingForm
from .models import Patient, Doctor, Nurse, Appointment, MedicalRecord, Billing

# Create your views here.
def dashboard(request):
    # Total patients
    total_patients = Patient.objects.count()
    # Total doctors
    total_doctors = Doctor.objects.count()
    # Total nurses
    total_nurses = Nurse.objects.count()
    # Total appointments
    total_appointments = Appointment.objects.count()
    # Total revenue
    total_revenue = Billing.objects.aggregate(total=Sum('amount'))['total'] or 0
    # Pending bills
    pending_bills = Billing.objects.filter(payment_status='Pending').count()

    # Patients registered in the last 7 days
    patients_registration_data = []
    patients_registration_labels = []
    for i in range(6, -1, -1):
        date = datetime.today() - timedelta(days=i)
        count = Patient.objects.filter(created_at__date=date).count()
        patients_registration_data.append(count)
        patients_registration_labels.append(date.strftime('%a'))

    # Appointment data (example, you need to define how to get this data)
    appointment_data = [10, 20, 30, 40, 50, 60, 70]  # Replace with actual data
    appointment_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']  # Replace with actual labels

    # Billing overview
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
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient_add.html', {'form': form})

def doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor_add.html', {'form': form})

def nurse(request):
    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nurse_list')
    else:
        form = NurseForm()
    return render(request, 'nurse_add.html', {'form': form})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_add.html', {'form': form})

def medical(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_list')
    else:
        form = MedicalRecordForm()
    return render(request, 'medical_add.html', {'form': form})

def bill(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillingForm()
    return render(request, 'bill_add.html', {'form': form})