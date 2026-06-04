from django.urls import path
from .views import *

urlpatterns = [
    path("success_url/", success_esewa, name='success'),
    path("failure_url/", failure_esewa, name='failure'),

]
