from django.urls import path, include
from django.views.generic import TemplateView

from .views import register, add_scheme, schemas, download_csv

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('register/', register, name='register'),
    path('add_schema/', add_scheme, name='add_scheme'),
    path('schemas/', schemas, name='schemas'),
    path('download-csv/', download_csv, name='download_csv'),
]
