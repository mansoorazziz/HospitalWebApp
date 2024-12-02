from django import forms
from .models import Medicine, LabTest

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'morning', 'afternoon', 'evening', 'night']

class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ['name']
