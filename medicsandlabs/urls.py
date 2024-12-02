from django.urls import path
from . import views

urlpatterns = [
    # Medicine URLs
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicines/create/', views.medicine_create, name='medicine_create'),
    path('medicines/update/<int:id>/', views.medicine_update, name='medicine_update'),
    path('medicines/delete/<int:id>/', views.medicine_delete, name='medicine_delete'),
    
    # Lab Test URLs
    path('labtests/', views.labtest_list, name='labtest_list'),
    path('labtests/create/', views.labtest_create, name='labtest_create'),
    path('labtests/update/<int:id>/', views.labtest_update, name='labtest_update'),
    path('labtests/delete/<int:id>/', views.labtest_delete, name='labtest_delete'),
]
