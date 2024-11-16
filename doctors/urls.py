from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_doctor, name='add_doctor'),
    path('', views.doctor_list, name='doctor_list'),  # Assuming you have a list view
]
