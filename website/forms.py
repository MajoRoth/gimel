from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'שם'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'טלפון'} ))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'מייל'}))
    text = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'input100', 'placeholder': 'טקסט'}))
