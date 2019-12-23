from django.contrib import admin
from .models import City, Area, Locality

admin.site.register(City)
admin.site.register(Locality)
admin.site.register(Area)
