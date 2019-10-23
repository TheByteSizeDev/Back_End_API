from django.db import models
from .daddy_o import Daddy_O
from .difficulty_type import Difficulty_Type

class Moves(models.Model):
    """Model for Moves"""
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=400)
    daddy_o = models.ForeignKey(Daddy_O, on_delete = models.CASCADE)
    difficulty_type = models.ForeignKey(Difficulty_Type, on_delete = models.DO_NOTHING)
    situation_items = models.ManyToManyField("Situation", through="Move_Situation_Relationship")
    body_region_items = models.ManyToManyField("Body_Region", through="Move_Bodyregion_Relationship")

    class Meta:
        verbose_name = ("move")
        verbose_name_plural = ("moves")