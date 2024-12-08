from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/edit/<int:serial_no>/', views.edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:serial_no>/', views.delete_appointment, name='delete_appointment'),


    # ------------------------------------------------Prescription URL--------------------------------------------
    path('prescription/<int:serial_no>/', views.prescription_view, name='prescription_view'),
]
