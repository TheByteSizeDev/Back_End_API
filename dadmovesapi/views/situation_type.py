"""View module for handling requests about situation types"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Situation_Types


class Situation_Type_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for dadmoves the situation type of each move
    Arguments:
        serializers
    """
    class Meta:
        model = Situation_Types
        url = serializers.HyperlinkedIdentityField(
            view_name='situation_type',
            lookup_field='id'
        )
        fields = ('id', 'url', 'situation' )


class Situation_Type(ViewSet):
    """Situation types for DadMoves Api"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single situation type
        Returns:
            Response -- JSON serialized situation type instance
        """
        try:
            situation_type = Situation_Type.objects.get(pk=pk)
            serializer = Situation_Type_Serializer(
                situation_type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to situation type resource
        Returns:
            Response -- JSON serializer list of situation types
        """
        situation_type = Situation_Types.objects.all()

        serializer = Situation_Type_Serializer(
            situation_type, many=True, context={'request': request})
        return Response(serializer.data)
