from django import forms
from .models import TimeSuggestion


class TimeSuggestionAddForm(forms.ModelForm):

    fajar = forms.TimeField(input_formats=["%I:%M %p"])
    zuhar = forms.TimeField(input_formats=["%I:%M %p"])
    asar = forms.TimeField(input_formats=["%I:%M %p"])
    maghrib = forms.TimeField(input_formats=["%I:%M %p"])
    isha = forms.TimeField(input_formats=["%I:%M %p"])
    juma = forms.TimeField(input_formats=["%I:%M %p"])

    class Meta:
        model = TimeSuggestion
        fields = ("masjid", "fajar", "zuhar", "asar", "maghrib", "isha", "juma")
        labels = {
            "user_name": "your name",
            "user_phone": "your phone"
        }
