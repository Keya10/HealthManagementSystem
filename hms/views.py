from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientForm, DoctorForm, NurseForm, AppointmentForm, MedicalRecordForm, BillingForm
from .models import Patient, Doctor, Nurse, Appointment, MedicalRecord, Billing


# Create your views here.
def home(request):
    return render(request, 'home.html')    # This is a simple HttpResponse


def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient_add.html', {'form': form})
        

#add doctor
def doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor_add.html', {'form': form})    # This is a simple HttpResponse

#add nurse
def nurse(request):
    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nurse_list')
    else:
        form = NurseForm()
    return render(request, 'nurse_add.html', {'form': form})    # This is a simple HttpResponse

#add appointment
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_add.html', {'form': form})    # This is a simple HttpResponse


#add medical record
def medical(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_list')
    else:
        form = MedicalRecordForm()
    return render(request, 'medical_add.html',{'form': form})    # This is a simple HttpResponse

#add bill
def bill(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillingForm()
    return render(request, 'bill_add.html', {'form': form})    # This is a simple HttpResponse

form = PatientForm()
print(form.fields.keys())  # This will print available fields
