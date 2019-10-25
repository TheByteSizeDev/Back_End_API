from django.db import models
from .daddy_o import Daddy_O
from .difficulty_type import Difficulty_Type
from .body_region import Body_Region
from .situation_type import Situation_Type

class Moves(models.Model):
    """Model for Moves"""
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=400)
    daddy_o = models.ForeignKey(Daddy_O, on_delete = models.CASCADE)
    difficulty_type = models.ForeignKey(Difficulty_Type, on_delete = models.DO_NOTHING)
    situation_type = models.ForeignKey(Situation_Type, on_delete = models.DO_NOTHING)
    body_region = models.ForeignKey(Body_Region, on_delete = models.DO_NOTHING)

    class Meta:
        verbose_name = ("move")
        verbose_name_plural = ("moves")