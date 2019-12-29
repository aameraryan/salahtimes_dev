from django import forms
from .models import NewSuggestion, TimeSuggestion


class NewSuggestionAddForm(forms.ModelForm):

    class Meta:
        model = NewSuggestion
        fields = ("user_name", "user_phone", "area", "address", "fajar", "zuhar", "asar", "maghrib", "isha", "juma")
        labels = {
            "user_name": "your name",
            "user_phone": "your phone"
        }


class TimeSuggestionAddForm(forms.ModelForm):

    class Meta:
        model = TimeSuggestion
        fields = ("user_name", "user_phone", "masjid", "fajar", "zuhar", "asar", "maghrib", "isha", "juma")
        labels = {
            "user_name": "your name",
            "user_phone": "your phone"
        }
