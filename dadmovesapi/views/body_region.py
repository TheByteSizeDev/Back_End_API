"""View module for handling requests about body region"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Body_Region


class Body_Region_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for dadmoves body region of each move
    Arguments:
        serializers
    """
    class Meta:
        model = Body_Region
        url = serializers.HyperlinkedIdentityField(
            view_name='body_region',
            lookup_field='id'
        )
        fields = ('id', 'url', 'region' )


class Body_Region(ViewSet):
    """Body region for DadMoves Api"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single body region
        Returns:
            Response -- JSON serialized body region instance
        """
        try:
            body_region = Body_Region.objects.get(pk=pk)
            serializer = Body_Region_Serializer(
                body_region, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to body region resource
        Returns:
            Response -- JSON serializer list of body region
        """
        body_region = Body_Region.objects.all()

        serializer = Body_Region_Serializer(
            body_region, many=True, context={'request': request})
        return Response(serializer.data)