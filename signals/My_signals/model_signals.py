from django.db.models.signals import *
from django.dispatch import receiver
from django.contrib.auth.models import User
from signals.models import student_data

object_student_data = student_data.objects.all()

"""pre_save signals"""


# for user
@receiver(pre_save, sender=User)
def beginning_save(sender, instance, **kwargs):
   print("-----pre save signal run")
   print("sender: ", sender)
   print("instance: ", instance)
   print(f'kwargs:  {kwargs}')


# for student
@receiver(pre_save, sender=student_data)
def beginning_save(sender, instance, **kwargs):
   print("pre save signal run--------------")
   print("sender: ", sender)
   print("instance: ", instance)
   print(f'kwargs:  {kwargs}')


# ---------------------------------------------------------------------------

"""post_save"""


@receiver(post_save, sender=student_data)
def ending_save(sender, instance, created, **kwargs):
   if created:  # if the data is just created craeted will be True
      print("------------post save signal run")
      print("created@! ")
      print("sender: ", sender)
      print("created: ", created)
      print("instance: ", instance)
      print(f'kwargs:  {kwargs}')
   else:
      print("------------post save signal run")
      print("Updated")
      print("sender: ", sender)
      print("created: ", created)
      print("instance: ", instance)
      print(f'kwargs:  {kwargs}')


# ---------------------------------------------------------------------------
"""pre delet"""


@receiver(pre_delete, sender=student_data)
def beginning_delete(sender, instance, **kwargs):
   print("Pre delete signal run--------------")
   print("delete started")
   print("sender: ", sender)
   print("instance:  ", instance)
   print(f'kwargs:  {kwargs}')


# ---------------------------------------------------------------------------
"""Post delet"""


@receiver(post_delete, sender=student_data)
def ending_delete(sender, instance, **kwargs):
   print("post delete signal run--------------")
   print("delete end!")
   print("sender: ", sender)
   print("instance:  ", instance)
   print(f'kwargs:  {kwargs}')


# ---------------------------------------------------------------------------
"""pre init"""


@receiver(pre_init, sender=User)
def model_pre_initialize(sender, *args, **kwargs):
   print("pre_init signal run--------------")
   print("initialize models started")
   print("sender: ", sender)
   print(f'kwargs:  {args}')
   # print("instance:  ",instance)
   print(f'kwargs:  {kwargs}')


# ---------------------------------------------------------------------------
"""post_init"""


@receiver(post_init, sender=User)
def model_post_initialize(sender, *args, **kwargs):
   print("post_init signal run--------------")
   print("initialize models end!! ")
   print("sender: ", sender)
   print(f'kwargs:  {args}')
   # print("instance:  ",instance)
   print(f'kwargs:  {kwargs}')
