from django.db import models

class User_details(models.Model):
     phone = models.TextField(blank=True,null=True)
     user_id = models.BigIntegerField(default=0)
     fb_details = models.TextField(blank=True, null=True)
