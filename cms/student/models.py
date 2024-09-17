from django.db import models

# Create your models here.
class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    course = models.CharField(max_length=100)


    def __str__(self):
        return self.email
   
