from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment

# Add new appointment
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/add_appointment.html', {'form': form})

# Appointments List
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

# Update appointment
def edit_appointment(request, serial_no):
    appointment = get_object_or_404(Appointment, serial_no=serial_no)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/edit_appointment.html', {'form': form})

# Delete appointment
def delete_appointment(request, serial_no):
    appointment = get_object_or_404(Appointment, serial_no=serial_no)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointments/delete_appointment.html', {'appointment': appointment})
