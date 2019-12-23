from django.db import models

# Create your models here.
class EmpDetails(models.Model):
    emp_id=models.IntegerField()
    firstname=models.CharField(max_length=256)
    lastname=models.CharField(max_length=256)
