from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    serial_no = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason_for_visit = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Scheduled')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment: {self.patient} with Dr. {self.doctor} on {self.appointment_date}"

