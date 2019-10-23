"""View module for handling requests about moves"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Moves, Daddy_O, Difficulty_Type, Situation_Type, Body_Region
from .situation_type import Situation_Type_Serializer
from .body_region import Body_Region_Serializer

class Moves_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for dadmoves dance moves
    Arguments:
        serializers
    """
    situation_items = Situation_Type_Serializer(many=True)
    body_region_items = Body_Region_Serializer(many=True)

    class Meta:
        model = Moves
        url = serializers.HyperlinkedIdentityField(
            view_name='move',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'link', 'daddy_o_id', 'difficulty_type', 'situation_items', 'body_region_items')
        depth = 1


class Move(ViewSet):
    """Moves for DadMoves Api"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Move instance
        """
        new_move = Moves()

        # FIXME: This needs to be looked over again once I get  to the front end add

        # for item in "situation_id":
        #     situation_item = Move_Situation_Relationship()
        #     situation_item.situation = Situation_Types.objects.get(pk=request.data["situation_id"])
        #     situation_item.move = new_move
        #     situation_item.save()

        # for item in "bodyregion_id":
        #     body_region_item = Move_Bodyregion_Relationship()
        #     body_region_item.region = Body_Region.objects.get(pk=request.data["body_region_id"])
        #     body_region_item.move = new_move
        #     body_region_item.save()         

        new_move.daddy_o = Daddy_O.objects.get(user=request.auth.user)
        new_move.difficulty_type = Difficulty_Type.objects.get(
            pk=request.data['difficulty_type'])

        new_move.name = request.data["name"]
        new_move.link = request.data["link"]
        new_move.save()

        # Then some how I take all_situations and all_body_regions then make then into their own shit through the serializer

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
        daddy_o = Daddy_O.objects.get(user=request.auth.user)
        updated_move.daddy_o= daddy_o
        difficulty_type = Difficulty_Type.objects.get(
            pk=request.data['difficulty_type'])
        updated_move.difficulty_type = difficulty_type
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
