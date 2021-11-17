from django.contrib.auth.signals import user_logged_in,user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from signals.models import LOG_IN_SIGNALS,LOG_OUT_SIGNALS,LOGIN_FAILED


#1 define reciver function
#3 we connect it with using decorator
@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
   LOG_IN_SIGNALS.objects.create(
      sender=sender,
      request_path=str(request)[14:-2],
      username=user
   )

   print("------------loggedin signal run-------------------")
   print("sender: ",sender)
   print("request: ",request)
   print("user data: ",user)
   print(f'kwargs:  {kwargs}')



#2 connect the singla with reciver
#user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out,sender=User)
def logout_success(sender,request,user,**kwargs):
   LOG_OUT_SIGNALS.objects.create(
      sender=sender,
      request_path=str(request)[14:-2],
      username=user
   )
   print("------------logout signal run-------------------")
   print("sender: ", sender)
   print("request: ", request)
   print("user data: ", user)
   print(f'kwargs:  {kwargs}')

#user_logged_out.connect(logout_success,sender=User)


def login_failed(sender,credentials,request,**kwargs):
   LOGIN_FAILED.objects.create(
      sender=sender,
      request_path=str(request)[14:-2],
      username=credentials['username']
   )
   #print(credentials)
   print("------------Failed to log in-------------------")
   print("sender: ", sender)
   print("request: ", request)
   print("user data: ", credentials['username'])
   print(f'kwargs:  {kwargs}')

user_login_failed.connect(login_failed)



