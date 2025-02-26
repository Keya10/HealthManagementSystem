
#  Health Management System

The Health Management System (HMS) is a web-based application builed usind django framework designed to streamline healthcare operations in Kenya. The system will enable hospitals, clinics, and medical practitioners to manage patient records, appointments, billing, prescriptions, and reporting efficiently.



## Features

- Patient Registration: Capture and store patient demographics, medical history, and contact details.
- Electronic Health Records (EHR): Maintain comprehensive and secure digital records of patient visits, diagnoses, treatments, and lab results.
- Patient Search: Quickly retrieve patient records using search filters like name, ID, or phone number.
- Medical History Tracking: Track and display a patient’s medical history, including allergies, chronic conditions, and past treatments.
- Online Booking: Allow patients to book appointments online via a patient portal.
- Appointment Management: Enable healthcare providers to schedule, reschedule, or cancel appointments.
- Billing System: Generate and manage invoices for consultations, tests, procedures, and medications.
- Receipts: Automatically generate and issue receipts for payments made.

- Custom Reports: Generate reports on patient visits, revenue, appointments
- User Authentication: Secure login with multi-factor authentication (MFA) for enhanced security.
- Responsive Design: Ensure the system is accessible and functional on mobile devices.

- Mobile App Integration: Option to integrate with a mobile app for on-the-go access.

- Staff Management: Manage staff schedules, roles, and performance.

- Compliance Reporting: Generate reports for regulatory compliance and audits.

## Technology Used

- Backend: Django Rest Framework, Python
- Frontend: HTML, CSS (Bootstrap)
- Data Visualization: Morris charts
- Database: SQLite (can be extended to other databases supported by Django)
- Deployment: Django's built-in development server (can be deployed on platforms like AWS, Heroku, etc.)

## Setup Instructions
1. Install Python: Make sure Python is installed on your system. You can download it from python.org and follow the installation instructions.
2. Create a Virtual Environment: It's recommended to use a virtual environment to manage dependencies for your Django project.
```
# Install virtualenv if you haven't already
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment (on Windows)
venv\Scripts\activate

# Activate the virtual environment (on macOS/Linux)
source venv/bin/activate
```
3. Install Django and Django Rest Framework:

```   # Install Django and Django Rest Framework using pip.
    pip install django djangorestframework
```
4. Clone and Setup Your Project:
```
 # https://github.com/Keya10/HEALTH-MANAGEMENT-SYSTEM.git
 cd HEALTH-MANAGEMENT-SYSTEM
 ```
 5. Create a Superuser
 ``` 
 python manage.py createsuperuser
 ```
 6. Run Development server
 ``` 
 python mange.py runserver
 ```
 
![Image 1](1.png)
![Image 2](2.png)




