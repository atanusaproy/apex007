from django.db import models

class User_details(models.Model):
     phone = models.IntegerField(blank=True,null=True)
     user_id = models.BigIntegerField(default=0)