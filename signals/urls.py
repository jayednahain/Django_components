
from django.urls import path
from .views import test_request_exception_signals



urlpatterns = [
    path('',test_request_exception_signals,name="test_signals"),
]