from django.db import models
from django.contrib.auth.models import User as Usr
# Create your models here.


class User(Usr):

    def __str__(self):
        return "@{}".format(self.username)


