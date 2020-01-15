from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from masjids.models import Masjid

from suggestions.models import NewSuggestion, TimeSuggestion
from .forms import TimeSuggestionAddForm


class TimeSuggestionAddView(CreateView):
    model = TimeSuggestion
    form_class = TimeSuggestionAddForm
    template_name = "suggestions/time_suggestion_add.html"
    success_url = reverse_lazy("portal:home")

    def form_valid(self, form):
        messages.success(self.request, "Thanks! Suggestion added successfully, We will look on it.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        try:
            masjid = Masjid.objects.get(id=self.request.GET['msid'])
            context['masjid'] = masjid
        except:
            pass
        return context


