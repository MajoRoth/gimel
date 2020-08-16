from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from website.settings import MEDIA_ROOT
import os
import misaka
from django.utils import timezone


# Create your models here.
class News(models.Model):
    # An order from warehouse !!!
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', null=True, blank=True, default='media/default.jpeg')
    text = models.TextField()
    text_html = models.TextField(null=True)
    pub_date = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        self.text_html = misaka.html(self.text)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('News:index')
