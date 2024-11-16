from django.db import models
from patients.models import Patient
from appointments.models import Appointment

class Billing(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Overdue', 'Overdue'),
    ]

    serial_no = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)
    date_of_bill = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Bill {self.serial_no} for {self.patient} - {self.status}"
