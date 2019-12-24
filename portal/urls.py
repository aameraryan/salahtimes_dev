from django.conf.urls import url
from . import views

app_name = "portal"

urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^search/$', views.search, name="search"),

]
