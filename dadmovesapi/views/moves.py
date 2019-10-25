"""View module for handling requests about moves"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Moves, Daddy_O, Difficulty_Type, Situation_Type, Body_Region

class Moves_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for dadmoves dance moves
    Arguments:
        serializers
    """

    class Meta:
        model = Moves
        url = serializers.HyperlinkedIdentityField(
            view_name='move',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'link', 'daddy_o_id', 'difficulty_type', 'difficulty_type_id', 'situation_type_id', 'situation_type', 'body_region_id', 'body_region')
        depth = 1


class Move(ViewSet):
    """Moves for DadMoves Api"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Move instance
        """
        new_move = Moves()        

        new_move.daddy_o = Daddy_O.objects.get(user=request.auth.user)
        new_move.difficulty_type = Difficulty_Type.objects.get(
            pk=request.data['difficulty_type'])
        new_move.situation_type = Situation_Type.objects.get(
            pk=request.data['situation_type'])
        new_move.body_region= Body_Region.objects.get(
            pk=request.data['body_region'])

        new_move.name = request.data["name"]
        new_move.link = request.data["link"]
        new_move.save()

        serializer = Moves_Serializer(
            new_move, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single move
        Returns:
            Response -- JSON serialized move instance
        """
        try:
            move = Moves.objects.get(pk=pk)
            serializer = Moves_Serializer(
                move, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an individual move
        Returns:
            Response -- Empty body with 204 status code
        """
        updated_move = Moves.objects.get(pk=pk)

        updated_move.name = request.data["name"]
        updated_move.daddy_o = Daddy_O.objects.get(user=request.auth.user)
        updated_move.difficulty_type = Difficulty_Type.objects.get(
            pk=request.data['difficulty_type'])
        updated_move.situation_type = Situation_Type.objects.get(
            pk=request.data['situation_type'])
        updated_move.body_region= Body_Region.objects.get(
            pk=request.data['body_region'])
        updated_move.link = request.data["link"]
        updated_move.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single move
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            deleted_move= Moves.objects.get(pk=pk)
            deleted_move.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Moves.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to moves resource
        Returns:
            Response -- JSON serializer list of moves
        """
        moves = Moves.objects.all()

        serializer = Moves_Serializer(
            moves, many=True, context={'request': request})
        return Response(serializer.data)
