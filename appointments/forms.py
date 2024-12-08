from django import forms
from .models import Appointment,Prescription


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'reason_for_visit', 'status', 'notes']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# ------------------------------------------------Prescription Form--------------------------------------------
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['medication', 'labtest', 'dosage', 'instructions']
        widgets = {
            'medication': forms.Select(attrs={'class': 'form-control select2'}),
            'labtest': forms.Select(attrs={'class': 'form-control select2'}),
        }
