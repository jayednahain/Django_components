from django.core.signals import *
from django.dispatch import receiver

@receiver(request_started)
def request_started(sender,environ,**kwargs):
   print("request-signal--started------------------")
   print("Sender: ",sender)
   print("Environ: ",environ)
   print(f'kwargs: {kwargs}')
# ---------------------------------------------------------------------------
@receiver(got_request_exception)
def request_exceptions(sender,request,**kwargs):
   print("--------------------------------------------------------------------------request exception accured signal run! ")
   print("Sender : ", sender)
   print("request : ",request)
   print(f'kwargs : {kwargs}')
# ---------------------------------------------------------------------------

@receiver(request_finished)
def request_finished(sender,**kwargs):
   print("----------------request-signal-finished")
   print("Sender: ",sender)
   print(f'kwargs: {kwargs}')