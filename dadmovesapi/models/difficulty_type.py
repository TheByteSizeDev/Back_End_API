from django.db import models

class Difficulty_Type(models.Model):
    """Model for Difficulty Types"""
    level = models.CharField(max_length=30)

    class Meta:
        verbose_name = ("difficulty_type")
        verbose_name_plural = ("difficulty_types")