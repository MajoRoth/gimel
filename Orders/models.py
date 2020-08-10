from django.db import models
from Accounts.models import User
from django.urls import reverse


# Create your models here.


class Worder(models.Model):
    # An order from warehouse !!!
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    date = models.DateTimeField()
    Approved = models.BooleanField()
    Active = models.BooleanField(default=True) # instead of deleting - set false

    def approve(self):
        self.Approved = True

    def __str__(self):
        return self.user.get_username() + "\n" + self.description

    def get_absolute_url(self):
        return reverse('Worder.views.details', args=[str(self.id)])


class Torder(models.Model):
    # An order from tahzooka !!!
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    date = models.DateTimeField()
    Approved = models.BooleanField()
    Active = models.BooleanField(default=True) # instead of deleting - set false

    def approve(self):
        self.Approved = True

    def __str__(self):
        return self.user.get_username() + "\n" + self.description

    def get_absolute_url(self):
        return reverse('Torder.views.details', args=[str(self.id)])


class Aorder(models.Model):
    ListOfAreas = [
        ('AU', 'אולם'), # Auditorium
        ('CO', 'מגרש'), # Court
        ('BY', 'מערום'), # Back Yard
        ('WO', 'חורשה'), # Woods
    ]
    # An area order !!!
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    area = models.CharField(
        max_length=2,
        choices=ListOfAreas,
        default='CO')

    date = models.DateTimeField()
    Approved = models.BooleanField()
    Active = models.BooleanField(default=True) # instead of deleting - set false

    def approve(self):
        self.Approved = True

    def __str__(self):
        return self.user.get_username() + "\n" + self.area

    def get_absolute_url(self):
        return reverse('Aorder.views.details', args=[str(self.id)])






