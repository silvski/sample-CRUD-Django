'''This module contains the classes needed to
create a form for the GuestInfo model.'''

from django import forms
from .models import GuestInfo

class GuestForm(forms.ModelForm):
    '''Creates a form for the GuestInfo model.
    '''
    class Meta:
        model = GuestInfo
        fields = '__all__'
        labels = {
            "f_name": "First Name",
            "m_name": "Middle Name",
            "l_name": "Last Name",
            "birth_date": "Date of Birth (YYYY-MM-DD)"
        }
    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
