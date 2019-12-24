from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from masjids.models import Masjid
from django.db.models import Q
from django.shortcuts import redirect


class HomeView(TemplateView):

    template_name = "portal/home.html"

    def get_context_data(self, **kwargs):
        masajid = Masjid.objects.all()
        context = super().get_context_data()
        context['masajid'] = masajid
        return context


def search(request):
    if request.method == "GET":
        queries = request.GET["query"]#.split(" ")
        # print(queries, "------------------------------------------------------------------------------------------------")
        results = Masjid.objects.filter(Q(name__icontains=queries) | Q(address__icontains=queries))
        print(results)
        return redirect("portal:home")
    return redirect("portal:home")
