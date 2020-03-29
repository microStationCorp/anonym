from django.urls import path
from django.shortcuts import redirect
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('<str:username>', views.messagePage),
    path('', RedirectView.as_view(url='../'))
]
