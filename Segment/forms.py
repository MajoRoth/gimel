from django import forms
from Segment.models import Segment
from django.contrib.auth.models import User

def get_name(self):
    return '{} {}'.format(self.first_name, self.last_name)


User.add_to_class("__str__", get_name)


class SegmentForm(forms.ModelForm):
    class Meta:
        model = Segment
        fields = ['user', 'segment', 'date']
        widgets = {
            'user': forms.Select(),
            'segment': forms.Select(),
            'date': forms.SelectDateWidget()
        }