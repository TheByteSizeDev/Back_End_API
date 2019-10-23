from django.db import models
from .daddy_o import Daddy_O
from .moves import Moves

class Dad_Moves_Relationship(models.Model):
    """Model for Relationship between daddy-os and their moves"""
    daddy_o = models.ForeignKey(Daddy_O, on_delete = models.CASCADE)
    move = models.ForeignKey(Moves, on_delete = models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    is_no_go = models.BooleanField(default=False)
    notes = models.CharField(max_length=300)

    class Meta:
        verbose_name = ("dad_moves_relationship")
        verbose_name_plural = ("dad_moves_relationships")