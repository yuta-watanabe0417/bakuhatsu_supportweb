from django.urls import path
from .views import ContactCreate

urlpatterns = [
  path('new/', ContactCreate.as_view(), name='contact_form'),
]