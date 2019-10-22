from django.db import models

class Situation_Types(models.Model):
    """Model for Situation Types"""
    situation = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("situation_type")
        verbose_name_plural = ("situation_types")