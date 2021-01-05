from django.db import models


# Create your models here.
class Student(models.Model):
    objects = None
    DoesNotExist = None
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30, default=None, blank=True, null=True)
    registrationDate = models.DateField()
