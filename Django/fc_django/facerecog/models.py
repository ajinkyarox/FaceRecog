from django.db import models

# Create your models here.
class EmpDetails(models.Model):

    firstname=models.CharField(max_length=256)
    lastname=models.CharField(max_length=256)

    class Meta:
        db_table = "EmpDetails"

class Photos(models.Model):
    pid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    photo=models.CharField(max_length=65535)

    class Meta:
        db_table = "Photos"