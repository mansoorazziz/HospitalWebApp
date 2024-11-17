from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_doctor, name='add_doctor'), # Add Doctor
    path('', views.doctor_list, name='doctor_list'),  # list view Doctor
    path('delete/<int:serial_no>/',views.delete_doctor, name='delete_doctor'), # Delete Doctor
    path('edit/<int:serial_no>/',views.edit_doctor, name='edit_doctor'), # Update Doctor
]
