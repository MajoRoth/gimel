from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Segment (models.Model):

    class SegmentChoices(models.TextChoices):
        AU = 'TU', _('שירותים')
        CO = 'JU', _('חדר זבל')
        BY = 'CO', _('מגרש')
        WO = 'TR', _('טריבונות')

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    date = models.DateField(default=timezone.now())
    segment = models.CharField(
        max_length=2,
        choices=SegmentChoices.choices,
        default=SegmentChoices.CO)

    Approved = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)  # instead of deleting - set false

    def get_absolute_url(self):
        # We will change to the list view once created
        return reverse('Segment:admin')

    def __str__(self):
        return "{} {}".format(self.user, self.segment)

    def approve(self):
        self.Approved = True
        self.save()

    def disapprove(self):
        self.Approved = False
        self.save()

    def disactive(self):
        self.Active = False
        self.save()





