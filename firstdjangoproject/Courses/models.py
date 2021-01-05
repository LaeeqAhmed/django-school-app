from django.db import models

# Create your models here.
class Course(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=100)
    credits = models.IntegerField()
