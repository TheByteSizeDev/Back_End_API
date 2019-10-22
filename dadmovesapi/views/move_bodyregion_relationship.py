"""View module for handling requests about the move body region relationship"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Move_Bodyregion_Relationship, Moves, Body_Region

class Move_Bodyregion_Relationship_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for the body region relationship with moves

    Arguments:
        serializers
    """
    class Meta:
        model = Move_Bodyregion_Relationship
        url = serializers.HyperlinkedIdentityField(
            view_name='move_bodyregion_relationship',
            lookup_field='id'
        )
        fields = ('id', 'body_region', 'move')
        depth = 1
        
        
class Move_Bodyregion_Relationship(ViewSet):
    """body region relationship for DadMoves"""
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized body region relationship instance
        """
        new_move_bodyregion_relationship = Move_Bodyregion_Relationship()
        
        body_region = Body_Region.get(pk=request.data['body_region_id'])
        new_move_bodyregion_relationship.body_region = body_region
        move = Moves.get(pk=request.data['move_id'])
        new_move_bodyregion_relationship.move = move
        new_move_bodyregion_relationship.save()
        
        serializer = Move_Bodyregion_Relationship_Serializer(new_move_bodyregion_relationship, context={'request': request})
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single move & body region relationship

        Returns:
            Response -- JSON serialized move & body region relationship instance
        """
        try:
            move_bodyregion_relationship = Move_Bodyregion_Relationship.objects.get(pk=pk)
            serializer = Move_Bodyregion_Relationship_Serializer(
                move_bodyregion_relationship, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def update(self, request, pk=None):
        """Handle PUT requests for a move & body region relationship

        Returns:
            Response -- Empty body with 204 status code
        """
        updated_move_bodyregion_relationship = Move_Bodyregion_Relationship.objects.get(pk=pk)
        body_region = Body_Region.objects.get(pk=request.data['body_region_id'])
        updated_move_bodyregion_relationship.body_region = body_region
        move = Moves.objects.get(pk=request.data['move_id'])
        updated_move_bodyregion_relationship.move = move
        updated_move_bodyregion_relationship.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single situation relationship with a move

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            Move_Bodyregion_Relationship.objects.get(pk=pk).delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except Move_Bodyregion_Relationship.DoesNotExist as ex:
             return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self, request):
        """Handle GET requests to move & body region relationship resource

        Returns:
            Response -- JSON serialized list of move & body region relationship
        """
        move_bodyregion_relationship = Move_Bodyregion_Relationship.objects.all()

        serializer = Move_Bodyregion_Relationship_Serializer(
            move_bodyregion_relationship, many=True, context={'request': request}
        )
        return Response(serializer.data)