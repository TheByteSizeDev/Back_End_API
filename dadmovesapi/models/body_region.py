from django.db import models

class Body_Region(models.Model):
    """Model for Body Regions"""
    region = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("body_region")
        verbose_name_plural = ("body_regions")