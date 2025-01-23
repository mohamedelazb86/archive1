from django.urls import path
from . import views

app_name='contractor'

urlpatterns = [
    path('contractor',views.contractor,name='contractor'),
    path('add-contractor',views.add_contractor,name='add-contractor'),
    path('delete-contractor',views.delete_contractor,name='delete-contractor'),
    path('edit-contractor',views.edit_contractor,name='edit-contractor'),
]
