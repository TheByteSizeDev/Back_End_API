"""View module for handling requests about difficulty types"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Difficulty_Type


class Difficulty_Type_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for dadmoves difficulty level of each move
    Arguments:
        serializers
    """
    class Meta:
        model = Difficulty_Type
        url = serializers.HyperlinkedIdentityField(
            view_name='difficulty_type',
            lookup_field='id'
        )
        fields = ('id', 'url', 'level' )


class Difficulty_Type(ViewSet):
    """Difficulty types for DadMoves Api"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single difficulty type
        Returns:
            Response -- JSON serialized difficulty type instance
        """
        try:
            difficulty_type = Difficulty_Type.objects.get(pk=pk)
            serializer = Difficulty_Type_Serializer(
                difficulty_type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to difficulty type resource
        Returns:
            Response -- JSON serializer list of difficulty types
        """
        difficulty_type = Difficulty_Type.objects.all()

        serializer = Difficulty_Type_Serializer(
            difficulty_type, many=True, context={'request': request})
        return Response(serializer.data)
