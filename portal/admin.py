from django.contrib import admin
from django.conf import settings

admin.site.site_header = settings.SITE_NAME
admin.site.site_title = settings.SITE_NAME
