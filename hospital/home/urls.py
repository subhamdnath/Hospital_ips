from home.views import *
from django.urls import re_path

urlpatterns = [
    
    re_path('^register/$', RegistrationApiView.as_view(), name="register_api" ),
]