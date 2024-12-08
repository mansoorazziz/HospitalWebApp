from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from medicsandlabs.models import Medicine, LabTest

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

# ------------------------------------------------Prescription Modal--------------------------------------------
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    labtest = models.ForeignKey(LabTest, on_delete=models.CASCADE, null=True, blank=True)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient} by Dr. {self.doctor} on {self.date}"
