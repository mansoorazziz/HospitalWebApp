from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm
from .models import Patient

# Adding new Patients
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # Redirect to a list view or another page after saving
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})

# Patients List
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

# Patient deletion
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients/delete_patient.html', {'patient': patient})

# Update Patient
def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/edit_patient.html', {'form': form, 'patient': patient})
