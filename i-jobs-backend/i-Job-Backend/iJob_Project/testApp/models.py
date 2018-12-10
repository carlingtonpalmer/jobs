from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    number = models.DateField(null=True)