from django.db import models
from django.core.validators import RegexValidator
from .models import Patient, Doctor, Nurse

class Patient(models.Model):
    national_id = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'^\d{1,10}$', message='Only digits are allowed')])
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(regex='^\+?1?\d{9,15}$', message='Phone number must be in the format: +254712345678.')])
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    blood_group = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        choices=[
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ]
    )
    medical_history = models.TextField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[RegexValidator(regex='^\+?1?\d{9,15}$', message='Phone number must be in the format: +254712345678.')]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.national_id})"

class Doctor(models.Model):
    national_id = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'^\d{1,10}$', message='Only digits are allowed')])
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(regex='^\+?1?\d{9,15}$', message='Phone number must be in the format: +254712345678.')])
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(regex='^[A-Za-z0-9]{5,20}$', message='License number must be alphanumeric and 5-20 characters long.')]
    )
    years_of_experience = models.PositiveIntegerField()
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"

#nurse models


class Nurse(models.Model):
    # Personal details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Professional details
    license_number = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(regex='^[A-Za-z0-9]{5,20}$', message='License number must be alphanumeric and 5-20 characters long.')]
    )
    #qualification = models.CharField(max_length=100, choices='RN' 'Registered Nurse', )  # e.g., Registered Nurse (RN), Enrolled Nurse (EN)
    years_of_experience = models.PositiveIntegerField()

    # Contact information
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex='^\+?1?\d{9,15}$', message='Phone number must be in the format: +254712345678.')]
    )
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)

    # Hospital/clinic details
    #hospital_name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)  # e.g., Maternity, ICU, General Ward

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nurse {self.first_name} {self.last_name}"

    #class Meta:
     #   verbose_name = "Nurse"
    #    verbose_name_plural = "Nurses"
    #    ordering = ['-created_at']

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for {self.patient} with Dr. {self.doctor} on {self.date} at {self.time}"

class MedicalRecord(models.Model):
    # Link to the patient
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')

    # Link to the doctor (who created the record)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='medical_records')

    # Medical details
    diagnosis = models.TextField()  # Diagnosis made by the doctor
    symptoms = models.TextField(blank=True, null=True)  # Symptoms reported by the patient
    treatment = models.TextField(blank=True, null=True)  # Treatment prescribed
    prescription = models.TextField(blank=True, null=True)  # Medications prescribed
    lab_results = models.TextField(blank=True, null=True)  # Lab test results
    notes = models.TextField(blank=True, null=True)  # Additional notes

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.last_name} ({self.created_at})"

class Billing(models.Model):
    # Link to the patient
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='bills')
    appointment = models.ForeignKey('Appointment', on_delete=models.SET_NULL, null=True, blank=True, related_name='bills')
    # Billing details
    bill_number = models.CharField(max_length=20, unique=True)  # Unique bill number
    DESCRIPTION_CHOISES = [
        ('Consultation Fee', 'Consultation Fee'),
        ('Lab Tests', 'Lab Tests'),
        ('Medication', 'Medication'),
        ('Other', 'Other'),
    ]
    description = models.TextField(max_length=20, choices=DESCRIPTION_CHOISES)  # Description of the bill (e.g., consultation fee, lab tests)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount to be paid
    date_issued = models.DateField(auto_now_add=True)  # Date the bill was issued
    due_date = models.DateField()  # Due date for payment

    # Payment details
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')

    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('M-Pesa', 'M-Pesa'),
        ('Insurance', 'Insurance'),
        ('Other', 'Other'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, blank=True, null=True)

    # M-Pesa transaction details (if applicable)
    mpesa_transaction_id = models.CharField(max_length=50, blank=True, null=True)  # M-Pesa transaction ID
    mpesa_transaction_date = models.DateTimeField(blank=True, null=True)  # Date of M-Pesa transaction

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bill #{self.bill_number} for {self.patient.first_name} {self.patient.last_name}"
