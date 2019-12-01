from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image = models.CharField(max_length=255, null=True)
    availability = models.CharField(max_length=255, default=0)
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, ('Inactive')),
        (ACTIVE, ('Active')),
    )
    status = models.IntegerField(default=0, choices=STATUS)