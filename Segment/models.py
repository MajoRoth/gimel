from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Segment (models.Model):

    class SegmentChoices(models.TextChoices):
        TU = 'TU', _('שירותים')
        JU = 'JU', _('חדר זבל')
        CO = 'CO', _('מגרש')
        TR = 'TR', _('טריבונות')
        GT = 'GT', _('מרצפות אפורות מחוץ לחדרים')
        TT = 'TT', _('מרצפות מחוץ לשירותים')
        GR = 'GR', _('חצץ')
        BI = 'BI', _('אופניים')
        HA = 'HA', _('חדר חמישיוט')
        TC = 'TC', _('החלפת פחים')
        SR = 'SR', _('חדר שכב״ג')
        HR = 'HR', _('חדר חיים')
        ZR = 'ZR', _('חדר צמיד')
        AU = 'AU', _('אולם')
        YT = 'YT', _('מרצפות צהובות')
        ES = 'ES', _('כניסה לשבט (מבפנים ומבחוץ)')
        PI = 'PI', _('מערום')
        WR = 'WR', _('חדר מחסן')
        KR = 'KR', _('חדר קיוסק')
        TG = 'TG', _('חדר תחזוקה')
        MR = 'MR', _('חדר מרכזים')

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





