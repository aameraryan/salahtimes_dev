from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from masjids.models import Masjid


class HomeView(TemplateView):

    template_name = "portal/home.html"

    def get_context_data(self, **kwargs):
        masajid = Masjid.objects.all()
        context = super().get_context_data()
        context['masajid'] = masajid
        return context
