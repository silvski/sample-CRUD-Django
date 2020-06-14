'''This module performs different CRUD operation.'''

from django.shortcuts import render, redirect
from .forms import GuestForm
from .models import GuestInfo

# Create your views here.
def guest_list(request):
    '''READ all rows from the guest database then display information.

    Parameters:
    -----------
        request: http request made by interacting with the web application.
    '''
    context = {'guest_list':GuestInfo.objects.all()}

    return render(request, "guest_register/guest_list.html", context)

def guest_form(request, id=0):
    '''CREATE or UPDATE a row in the guest database.

    Parameters:
    -----------
        request: http request made by the interacting with the web application.
        id_num: integer primary key to update; defaults to 0 for CREATE action.
    '''

    # For viewing
    if request.method == "GET":
        if id == 0:
            form = GuestForm()
        else:
            guest = GuestInfo.objects.get(pk=id)
            form = GuestForm(instance=guest)
        return render(request, "guest_register/guest_form.html", {'form':form})

    # For creating or updating
    else:
        if id == 0:
            form = GuestForm(request.POST)
        else:
            guest = GuestInfo.objects.get(pk=id)
            form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
        return redirect('/guest/list')

def guest_delete(request, id):
    '''DELETE the selected guest row from the database.

    Parameters:
    -----------
        request: http request made by the interacting with the web application.
        id_num: integer primary key to delete from the database.
    '''
    guest = GuestInfo.objects.get(pk=id)
    guest.delete()
    return redirect('/guest/list')
