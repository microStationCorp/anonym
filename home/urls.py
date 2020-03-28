from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage),
    path('login', include('login.urls')),
    path('signup', include('signup.urls'))
]
