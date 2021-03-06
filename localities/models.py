from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class City(models.Model):

    name = models.CharField(max_length=128)
    attribute_name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class Area(models.Model):

    city = models.ForeignKey(City, on_delete=models.CASCADE)

    name = models.CharField(max_length=128)
    pincode = models.PositiveIntegerField(validators=[MinValueValidator(limit_value=100000), MaxValueValidator(limit_value=999999)], unique=True)

    def __str__(self):
        return "{} {}".format(self.name, self.pincode)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"


