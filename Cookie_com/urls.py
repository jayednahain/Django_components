from django.urls import path,include
from Cookie_com.views import test
from Cookie_com.views.test import cookie_test
from Cookie_com.views.set_cookie import set_cookie_fun
from Cookie_com.views.get_cookie import get_cookie_fun
#from Cookie_com.views.del_cookie



urlpatterns = [

    path('',cookie_test,name='test_link'),
    path('set_cookie',set_cookie_fun,name='set_link'),
    path('get_cookie',get_cookie_fun,name='get_link'),



]