from django.db import models

# Create your models here.


class LOG_IN_SIGNALS(models.Model):
   sender       = models.CharField(max_length=50)
   request_path = models.CharField(max_length=50)
   username     = models.CharField(max_length=50)
   created_time = models.DateTimeField(auto_now_add=True)




class LOG_OUT_SIGNALS(models.Model):
   sender       = models.CharField(max_length=50)
   request_path = models.CharField(max_length=50)
   username     = models.CharField(max_length=50)
   created_time = models.DateTimeField(auto_now_add=True)


class LOGIN_FAILED(models.Model):
   sender       = models.CharField(max_length=50)
   request_path = models.CharField(max_length=50)
   username     = models.CharField(max_length=50)
   created_time = models.DateTimeField(auto_now_add=True)


class student_data(models.Model):
   name = models.CharField(max_length=20)
   section = models.CharField(max_length=10)
   exam_number = models.IntegerField()

   def __str__(self):
      return self.name
