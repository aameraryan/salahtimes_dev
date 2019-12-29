from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from suggestions.models import NewSuggestion, TimeSuggestion
from .forms import NewSuggestionAddForm, TimeSuggestionAddForm


class NewSuggestionAddView(CreateView):

    model = NewSuggestion
    form_class = NewSuggestionAddForm
    template_name = "suggestions/new_suggestion_add.html"
    success_url = reverse_lazy("portal:home")

    def form_valid(self, form):
        messages.success(self.request, "Thanks! Suggestion added successfully, We will look on it.")
        return super().form_valid(form)


class TimeSuggestionAddView(CreateView):
    model = TimeSuggestion
    form_class = TimeSuggestionAddForm
    template_name = "suggestions/time_suggestion_add.html"
    success_url = reverse_lazy("portal:home")

    def form_valid(self, form):
        messages.success(self.request, "Thanks! Suggestion added successfully, We will look on it.")
        return super().form_valid(form)
