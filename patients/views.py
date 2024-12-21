from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import PatientForm
from .models import Patient, ArchivedPatient

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
def delete_patient(request, serial_no):
    patient = get_object_or_404(Patient, serial_no=serial_no)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients/delete_patient.html', {'patient': patient})

# Update Patient
def edit_patient(request, serial_no):
    patient = get_object_or_404(Patient, serial_no=serial_no)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/edit_patient.html', {'form': form, 'patient': patient})

# Refresh Patient List
def refresh_patient_list(request):
    if request.method == 'POST':
        # Archive current patient list
        patients = Patient.objects.all()
        for patient in patients:
            ArchivedPatient.objects.create(
                serial_no=patient.serial_no,
                first_name=patient.first_name,
                last_name=patient.last_name,
                date_of_birth=patient.date_of_birth,
                medical_record=patient.medical_record,
                cnic_no=patient.cnic_no,
                gender=patient.gender
            )
        # Clear the patient list
        Patient.objects.all().delete()
        return JsonResponse({'message': 'Patient list refreshed successfully!'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

# Archived Patient list
def archived_patient_list(request):
    archived_patients = ArchivedPatient.objects.all()
    return render(request, 'patients/archived_patient_list.html', {'archived_patients': archived_patients})
