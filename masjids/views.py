from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Masjid
from django.urls import reverse_lazy
from django.contrib import messages


class MasjidCreateView(CreateView):

    model = Masjid
    fields = ("name", "area", "address", "fajar", "zuhar", "asar", "maghrib", "isha", "juma")
    template_name = "masjids/create.html"
    success_url = reverse_lazy("portal:home")

    def form_valid(self, form):
        messages.success(self.request, "Masjid entry has been created successfully. Thank you for your contribution.")
        return super().form_valid(form)

