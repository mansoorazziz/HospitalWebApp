from django.shortcuts import render, redirect, get_object_or_404
from .forms import DoctorForm
from .models import Doctor
from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# Create your views here.

# Adding new Doctors
@login_required
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Doctor added successfully!')
            # return redirect('add_doctor') # Redirect back to the same page to show the modal
            return redirect('doctor_list')  # Redirect to a list view or another page after saving
    else:
        form = DoctorForm()
    return render(request, 'doctors/add_doctor.html', {'form': form})



#  Doctors List
@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

# Doctor deletion
@login_required
def delete_doctor(request, serial_no):
    doctor = get_object_or_404(Doctor, serial_no=serial_no)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/delete_doctor.html', {'doctor': doctor})

# Update Doctor
@login_required
def edit_doctor(request, serial_no):
    doctor = get_object_or_404(Doctor, serial_no=serial_no)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/edit_doctor.html', {'form': form, 'doctor': doctor})

