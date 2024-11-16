from django.shortcuts import render, redirect
from .forms import DoctorForm
from .models import Doctor

# Create your views here.

# Adding new Doctors
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')  # Redirect to a list view or another page after saving
    else:
        form = DoctorForm()
    return render(request, 'doctors/add_doctor.html', {'form': form})



#  Doctors List
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})
