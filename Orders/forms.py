from django import forms
from Orders.models import Worder, Torder, Aorder


class WorderFrom(forms.ModelForm):
    class Meta:
        model = Worder
        fields = ['description', 'date']
        widgets = {
            'date': forms.SelectDateWidget()
        }


class TorderFrom(forms.ModelForm):
    class Meta:
        model = Torder
        fields = ['description', 'date']
        widgets = {
            'date': forms.SelectDateWidget()
        }


class AorderFrom(forms.ModelForm):
    class Meta:
        model = Aorder
        fields = ['area', 'date']
        widgets = {
            'date': forms.SelectDateWidget()
        }