from django.db import models
from .situation_type import Situation_Type
from .moves import Moves

class Move_Situation_Relationship(models.Model):
    """Model for Move Situtation Relationship"""
    situation = models.ForeignKey(Situation_Type, on_delete = models.CASCADE)
    move = models.ForeignKey(Moves, on_delete = models.CASCADE)

    class Meta:
        verbose_name = ("move_situation_relationship")
        verbose_name_plural = ("move_situation_relationships")