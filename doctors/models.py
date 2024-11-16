from django.db import models

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    SPECIALTY_CHOICES = [
        ('GP', 'General Practitioner'),
        ('Pediatrician', 'Pediatrician'),
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Neurologist', 'Neurologist'),
        ('Surgeon', 'Surgeon'),
        # Add more specialties as needed
    ]

    serial_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cnic_no = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    specialty = models.CharField(max_length=50, choices=SPECIALTY_CHOICES)
    date_hired = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialty}"
