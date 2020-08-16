from django import forms
from News.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['text', 'image']

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False


