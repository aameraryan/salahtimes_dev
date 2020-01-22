from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime

from localities.models import Area


class Masjid(models.Model):

    area = models.ForeignKey(Area, on_delete=models.PROTECT)

    name = models.CharField(max_length=256)
    address = models.TextField(blank=True)
    extra_info = models.TextField(blank=True)

    fajar = models.TimeField()
    zuhar = models.TimeField()
    asar = models.TimeField()
    maghrib = models.TimeField()
    isha = models.TimeField()
    juma = models.TimeField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def get_last_updated_text(self):
        last_updated = (timezone.now()-self.updated_on).days
        if last_updated == 0:
            text = "Today"
        elif last_updated == 1:
            text = "Yesterday"
        elif last_updated >= 30:
            text = "{} months ago".format(last_updated//30)
        else:
            text = "{} days ago".format(last_updated)
        return text

    def get_address_display(self):
        return "{}".format(self.address)

    class Meta:
        verbose_name = "Masjid"
        verbose_name_plural = "Masajid"
