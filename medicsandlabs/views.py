from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicine, LabTest
from .forms import MedicineForm, LabTestForm
from django.contrib.auth.decorators import login_required

# Medicine Views
@login_required
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicsandlabs/medicine_list.html', {'medicines': medicines})

@login_required
def medicine_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'medicsandlabs/medicine_form.html', {'form': form})


@login_required
def medicine_update(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'medicsandlabs/medicine_form.html', {'form': form})


@login_required
def medicine_delete(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')
    return render(request, 'medicsandlabs/medicine_confirm_delete.html', {'medicine': medicine})

# Lab Test Views
@login_required
def labtest_list(request):
    labtests = LabTest.objects.all()
    return render(request, 'medicsandlabs/labtest_list.html', {'labtests': labtests})


@login_required
def labtest_create(request):
    if request.method == 'POST':
        form = LabTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('labtest_list')
    else:
        form = LabTestForm()
    return render(request, 'medicsandlabs/labtest_form.html', {'form': form})


@login_required
def labtest_update(request, id):
    labtest = get_object_or_404(LabTest, id=id)
    if request.method == 'POST':
        form = LabTestForm(request.POST, instance=labtest)
        if form.is_valid():
            form.save()
            return redirect('labtest_list')
    else:
        form = LabTestForm(instance=labtest)
    return render(request, 'medicsandlabs/labtest_form.html', {'form': form})


@login_required
def labtest_delete(request, id):
    labtest = get_object_or_404(LabTest, id=id)
    if request.method == 'POST':
        labtest.delete()
        return redirect('labtest_list')
    return render(request, 'medicsandlabs/labtest_confirm_delete.html', {'labtest': labtest})
