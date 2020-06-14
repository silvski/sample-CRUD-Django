'''Initializes the models for the application.'''

from django.db import models

# Create your models here.
class GuestInfo(models.Model):
    '''Initializations of fields for the guest information.'''
    f_name = models.CharField(max_length=50)
    m_name = models.CharField(max_length=50, blank=True, null=True)
    l_name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateField()
    member = models.BooleanField()
    address = models.CharField(max_length=150)
    