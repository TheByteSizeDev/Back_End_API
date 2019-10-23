from django.db import models
from .body_region import Body_Region
from .moves import Moves

class Move_Bodyregion_Relationship(models.Model):
    """Model for move and body region relationship"""
    body_region = models.ForeignKey(Body_Region, on_delete = models.CASCADE)
    move = models.ForeignKey(Moves, on_delete = models.CASCADE)

    class Meta:
        verbose_name = ("body_region_item")
        verbose_name_plural = ("body_region_items")