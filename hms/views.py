from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum, Count
from datetime import datetime, timedelta
from .forms import PatientForm, DoctorForm, NurseForm, AppointmentForm, MedicalRecordForm, BillingForm
from .models import Patient, Doctor, Nurse, Appointment, MedicalRecord, Billing
from django.contrib.auth.decorators import login_required

# login view
def login_view(request):
    return render(request, 'registration/login.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {"form": form})

# Dashboard view
@login_required
def dashboard(request):
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_nurses = Nurse.objects.count()
    total_appointments = Appointment.objects.count()
    
    # Count appointments by status
    status_counts = Appointment.objects.values('status').annotate(count=Count('status'))
    status_counts_dict = {item['status']: item['count'] for item in status_counts}
    # Get counts for each status (default to 0 if no appointments exist for a status)
    pending_count = status_counts_dict.get('pending', 0)
    approved_count = status_counts_dict.get('approved', 0)
    completed_count = status_counts_dict.get('completed', 0)

    total_revenue = Billing.objects.aggregate(total=Sum('amount'))['total'] or 0
    pending_bills = Billing.objects.filter(payment_status='Pending').count()

    patients_registration_data = []
    patients_registration_labels = []
    for i in range(6, -1, -1):
        date = datetime.today() - timedelta(days=i)
        count = Patient.objects.filter(created_at__date=date).count()
        patients_registration_data.append(count)
        patients_registration_labels.append(date.strftime('%a'))

    appointment_data = [pending_count, approved_count, completed_count]  # Replace with actual data
    appointment_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']  # Replace with actual labels

    billing_labels = ['Paid', 'Pending']
    billing_data = [
        Billing.objects.filter(payment_status='Paid').count(),
        Billing.objects.filter(payment_status='Pending').count(),
    ]

    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_nurses': total_nurses,
        'total_appointments': total_appointments,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'completed_count': completed_count,
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

@login_required
def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully')
            return redirect('patient_list')
        else:
            messages.error(request, 'Invalid data. Please check the form')
    else:
        form = PatientForm()
    return render(request, 'patient_add.html', {'form': form})

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

@login_required
def patient_update(request, id):
    patient = get_object_or_404(Patient, pk=id)
    if request.method == 'POST':
        form = PatientForm(request.POST or None, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient updated successfully')
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient_update.html', {'form': form})

@login_required
def delete_patient(request, id):
    patient = get_object_or_404(Patient, pk=id)
    patient.delete()
    messages.success(request, 'Patient deleted successfully')
    return redirect('patient_list')

@login_required
def doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor added successfully')
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor_add.html', {'form': form})

@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

@login_required
def doctor_update(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST or None, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor updated successfully')
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_update.html', {'form': form})

@login_required
def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    doctor.delete()
    messages.success(request, 'Doctor deleted successfully')
    return redirect('doctor_list')

@login_required
def nurse(request):
    if request.method == 'POST':
        form = NurseForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nurse added successfully')
            return redirect('nurse_list')
    else:
        form = NurseForm()
    return render(request, 'nurse_add.html', {'form': form})

@login_required
def nurse_list(request):
    nurses = Nurse.objects.all()
    return render(request, 'nurse_list.html', {'nurses': nurses})

@login_required
def nurse_update(request, id):
    nurse = get_object_or_404(Nurse, pk=id)
    if request.method == 'POST':
        form = NurseForm(request.POST or None, instance=nurse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nurse updated successfully')
            return redirect('nurse_list')
    else:
        form = NurseForm(instance=nurse)
    return render(request, 'nurse_update.html', {'form': form})

@login_required
def delete_nurse(request, id):
    nurse = get_object_or_404(Nurse, pk=id)
    nurse.delete()
    messages.success(request, 'Nurse deleted successfully')
    return redirect('nurse_list')

@login_required
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment booked successfully')
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_add.html', {'form': form})


@login_required
def appointment_list(request):
    query = request.GET.get('q')
    if query:
        appointments = Appointment.objects.filter(patient__icontains=query)
    else:
        appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

@login_required
def appointment_update(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST or None, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully')
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_update.html', {'form': form})

@login_required
def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    appointment.delete()
    messages.success(request, 'Appointment deleted successfully')
    return redirect('appointment_list')

@login_required
def medical(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medical record added successfully')
            return redirect('medical_list')
    else:
        form = MedicalRecordForm()
    return render(request, 'medical_add.html', {'form': form})

@login_required
def medical_list(request):
    medical_records = MedicalRecord.objects.all()
    return render(request, 'medical_list.html', {'medical_records': medical_records})

@login_required
def medical_update(request, id):
    medical_record = get_object_or_404(MedicalRecord, pk=id)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST or None, instance=medical_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medical record updated successfully')
            return redirect('medical_list')
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'medical_update.html', {'form': form})

@login_required
def delete_medical(request, id):
    medical_record = get_object_or_404(MedicalRecord, pk=id)
    medical_record.delete()
    messages.success(request, 'Medical record deleted successfully')
    return redirect('medical_list')

@login_required
def bill(request):
    if request.method == 'POST':
        form = BillingForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bill added successfully')
            return redirect('bill_list')
    else:
        form = BillingForm()
    return render(request, 'bill_add.html', {'form': form})

@login_required
def bill_list(request):
    bills = Billing.objects.all()
    return render(request, 'bill_list.html', {'bills': bills})

@login_required
def bill_update(request, id):
    bill = get_object_or_404(Billing, pk=id)
    if request.method == 'POST':
        form = BillingForm(request.POST or None, instance=bill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bill updated successfully')
            return redirect('bill_list')
    else:
        form = BillingForm(instance=bill)
    return render(request, 'bill_update.html', {'form': form})

@login_required
def bill_delete(request, id):
    bill = get_object_or_404(Billing, pk=id)
    bill.delete()
    messages.success(request, 'Bill deleted successfully')
    return redirect('bill_list')
