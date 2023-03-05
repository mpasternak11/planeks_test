from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Scheme(models.Model):
    full_name = models.CharField(max_length=65, verbose_name='Full name')
    name_scheme = models.CharField(max_length=40, verbose_name='Name of scheme')
    job = models.CharField(max_length=100, verbose_name='Job')
    email = models.EmailField(verbose_name='Email')
    domain_name = models.CharField(max_length=100, verbose_name='Domain')
    company_name = models.CharField(max_length=30, verbose_name='Company name')
    text = models.TextField(max_length=255, verbose_name='Text')
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(65)])
    address = models.CharField(max_length=255, verbose_name='Address')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
