from django.urls import path,include
from Cookie_com.views import test
from Cookie_com.views.test import cookie_test

urlpatterns = [
    path('',cookie_test,name='test_link')
]