from django.db import models
from localities.models import Area


class NewSuggestion(models.Model):

    user_name = models.CharField(verbose_name="suggester name", max_length=64, blank=True)
    user_phone = models.CharField(verbose_name="suggester phone", max_length=13, blank=True)

    area = models.ForeignKey(Area, on_delete=models.PROTECT)

    name = models.CharField(max_length=256)
    address = models.TextField(blank=True)

    fajar = models.TimeField(blank=True)
    zuhar = models.TimeField(blank=True)
    asar = models.TimeField(blank=True)
    maghrib = models.TimeField(blank=True)
    isha = models.TimeField(blank=True)
    juma = models.TimeField(blank=True)

    staff_note = models.TextField(blank=True)

    suggested_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TimeSuggestion(models.Model):

    user_name = models.CharField(max_length=64, blank=True)
    user_phone = models.CharField(max_length=13, blank=True)

    masjid = models.ForeignKey("masjids.Masjid", on_delete=models.CASCADE)

    fajar = models.TimeField(blank=True)
    zuhar = models.TimeField(blank=True)
    asar = models.TimeField(blank=True)
    maghrib = models.TimeField(blank=True)
    isha = models.TimeField(blank=True)
    juma = models.TimeField(blank=True)

    staff_note = models.TextField(blank=True)

    suggested_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.masjid.name
