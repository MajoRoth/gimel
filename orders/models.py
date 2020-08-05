from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class WarehouseOrder(models.Model):

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    date = models.DateTimeField()
    

