import csv

from django.http import HttpResponse
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, AddSchemeForm, GenerateDataForm
from .models import Scheme


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def add_scheme(request):
    if request.method == 'POST':
        if 'generate_data' in request.POST:
            generate_form = GenerateDataForm(request.POST)
            if generate_form.is_valid():
                num_records = generate_form.cleaned_data['num_records']
                for i in range(num_records):
                    form = AddSchemeForm(request.POST, request.FILES)
                    if form.is_valid():
                        form.save()
                return redirect('home')
        else:
            form = AddSchemeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = AddSchemeForm()
        generate_form = GenerateDataForm()
    return render(request, 'add_scheme.html', {'form': form, 'generate_form': generate_form})


def schemas(request):
    schemes = Scheme.objects.all()
    context = {
        'schems': schemes,
    }
    return render(request, 'schemas.html', context=context)


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scheme.csv"'

    writer = csv.writer(response)
    writer.writerow(['Full name', 'Name of scheme', 'Job', 'Email', 'Domain', 'Company name', 'Text', 'Age', 'Address'])

    schemes = Scheme.objects.all().values_list('full_name', 'name_scheme', 'job', 'email', 'domain_name', 'company_name', 'text', 'age', 'address')
    for scheme in schemes:
        writer.writerow(scheme)

    return response
