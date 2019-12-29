from django.conf.urls import url
from . import views

app_name = "suggestions"

urlpatterns = [

    url(r'^new_suggestion/add/$', views.NewSuggestionAddView.as_view(), name="new_suggestion_add"),
    url(r'^time_suggestion/add/$', views.TimeSuggestionAddView.as_view(), name="time_suggestion_add"),

]
