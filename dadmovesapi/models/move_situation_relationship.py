from django.db import models
from .situation_type import Situation_Type
from .moves import Moves

class Move_Situation_Relationship(models.Model):
    """Model for Move Situtation Relationship"""
    situation_id = models.ForeignKey(Situation_Type, on_delete = models.CASCADE)
    move_id = models.ForeignKey(Moves, on_delete = models.CASCADE)

    class Meta:
        verbose_name = ("situation_item")
        verbose_name_plural = ("situation_items")