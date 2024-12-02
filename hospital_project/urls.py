from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=True)),  # Redirect to login page
    path('medicsandlabs/', include('medicsandlabs.urls')),
    # path('billing/', include('billing.urls')),
]
