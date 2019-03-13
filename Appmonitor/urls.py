from django.urls import path

from . import views

urlpatterns = [
    path('', views.Appmonitorsite, name='Appmonitorsite'),
]
