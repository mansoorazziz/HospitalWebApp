from django import forms
from .models import Appointment, Prescription

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'reason_for_visit', 'status', 'notes']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


# -------------------Prescription----------------------------------

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['medication', 'dosage', 'instructions']
