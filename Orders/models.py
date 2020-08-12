from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Worder(models.Model):
    # An order from warehouse !!!
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    date = models.DateField()
    Approved = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)  # instead of deleting - set false

    def approve(self):
        self.Approved = True

    def get_absolute_url(self):
        # We will change to the list view once created
        return reverse('home')


class Torder(models.Model):
    # An order from tahzooka !!!
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    date = models.DateField()
    Approved = models.BooleanField(default=False)
    Active = models.BooleanField(default=True) # instead of deleting - set false

    def approve(self):
        self.Approved = True

    def get_absolute_url(self):
        # We will change to the list view once created
        return reverse('home')


class Aorder(models.Model):
    ListOfAreas = [
        ('AU', 'אולם'), # Auditorium
        ('CO', 'מגרש'), # Court
        ('BY', 'מערום'), # Back Yard
        ('WO', 'חורשה'), # Woods
    ]
    # An area order !!!
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    area = models.CharField(
        max_length=2,
        choices=ListOfAreas,
        default='CO')

    date = models.DateField()
    Approved = models.BooleanField(default=False)
    Active = models.BooleanField(default=True) # instead of deleting - set false

    def approve(self):
        self.Approved = True

    def get_absolute_url(self):
        # We will change to the list view once created
        return reverse('home')





