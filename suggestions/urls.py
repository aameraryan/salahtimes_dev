from django.conf.urls import url
from . import views

app_name = "suggestions"

urlpatterns = [

    url(r'^time_suggestion/add/$', views.TimeSuggestionAddView.as_view(), name="time_suggestion_add"),

]
