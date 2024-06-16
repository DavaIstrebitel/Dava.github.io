from django import forms

class SchoolForm(forms.Form):
    CLASS_CHOICES = [
        ('9', '9 Класс'),
        ('11', '11 Класс'),
    ]
    REGION_CHOICES = [
        ('Москва', 'Москва'),
        ('Санкт-Петербург', 'Санкт-Петербург'),
        ('Новосибирск', 'Новосибирск'),
    ]

    selected_class = forms.ChoiceField(choices=CLASS_CHOICES, widget=forms.RadioSelect)
    region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select(attrs={'id': 'region'}))
    preferences = forms.CharField(widget=forms.Textarea, label='Предпочтения')
