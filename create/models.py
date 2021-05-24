from django.db import models

# Create your models here.
class TmpModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

class Meta:
    db_table = 'tmpmodel'
