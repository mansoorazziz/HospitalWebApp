from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/edit/<int:serial_no>/', views.edit_patient, name='edit_patient'),
    path('patients/delete/<int:serial_no>/', views.delete_patient, name='delete_patient'),
]