from django.db import models
from django.core.validators import RegexValidator

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

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=[
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ])