"""View module for handling requests about the move sitaution type relationship"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Move_Situation_Relationship, Moves, Situation_Types

class Move_Situation_Relationship_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for the situation type relationship with moves

    Arguments:
        serializers
    """
    class Meta:
        model = Move_Situation_Relationship
        url = serializers.HyperlinkedIdentityField(
            view_name='move_situation_relationships',
            lookup_field='id'
        )
        fields = ('id', 'situation', 'move')
        depth = 1
        
        
class Move_Situation_Relationships(ViewSet):
    """Situation type relationship for DadMoves"""
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized siutation & move relationship instance
        """
        new_move_situation_relationship = Move_Situation_Relationship()
        
        new_move_situation_relationship.situation = Situation_Types.get(pk=request.data['situation_id'])
        move = Moves.get(pk=request.data['move_id'])
        new_move_situation_relationship.move = move
        new_move_situation_relationship.save()
        
        serializer = Move_Situation_Relationship_Serializer(new_move_situation_relationship, context={'request': request})
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single move & situation type relationship

        Returns:
            Response -- JSON serialized move & situation type relationship instance
        """
        try:
            move_situation_relationship = Move_Situation_Relationship.objects.get(pk=pk)
            serializer = Move_Situation_Relationship_Serializer(
                move_situation_relationship, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def update(self, request, pk=None):
        """Handle PUT requests for a move & situation relationship

        Returns:
            Response -- Empty body with 204 status code
        """
        updated_move_situation_relationship = Move_Situation_Relationship.objects.get(pk=pk)
        situation = Situation_Types.objects.get(pk=request.data['situation_id'])
        updated_move_situation_relationship.situation = situation
        move = Moves.objects.get(pk=request.data['move_id'])
        updated_move_situation_relationship.move = move
        updated_move_situation_relationship.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single situation relationship with a move

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            Move_Situation_Relationship.objects.get(pk=pk).delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except Move_Situation_Relationship.DoesNotExist as ex:
             return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self, request):
        """Handle GET requests to move & situation type relationship resource

        Returns:
            Response -- JSON serialized list of move & situaton type relationship
        """
        move_situation_relationship = Move_Situation_Relationship.objects.all()

        serializer = Move_Situation_Relationship_Serializer(
            move_situation_relationship, many=True, context={'request': request}
        )
        return Response(serializer.data)