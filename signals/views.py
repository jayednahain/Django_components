from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def test_request_exception_signals(request):
   a = 10/0

   return HttpResponse("Hellow")