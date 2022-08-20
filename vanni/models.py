from django.db import models

# Create your models here.

class MobileMaster(models.Model):
    mobile_key=models.AutoField(primary_key=True)
    mobile=models.IntegerField(max_length=20)
    mobile_verified=models.BooleanField(default=False)

    class Meta:
        db_table='general.mobile_master'
