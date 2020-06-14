'''Routing URLS of different views.'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_form, name='guest_insert'), # get and post req. for insert operation
    path('<int:id>/', views.guest_form, name='guest_update'), # get and post req. for update operation
    path('list/', views.guest_list, name='guest_list'), # get req. for displaying records
    path('delete/<int:id>/', views.guest_delete, name='guest_delete')
]
