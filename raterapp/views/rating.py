"""View module for handling requests about ratings"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapp.models.gamer import Gamer
from raterapp.models.rating import Rating
from raterapp.models.game import Game



class RatingView(ViewSet):
    """Level up ratings view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single rating
        Returns:
            Response -- JSON serialized rating
        """
        try:
            rating = Rating.objects.get(pk=pk)
            serializer = RatingSerializer(rating)
            return Response(serializer.data)
        except Rating.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all ratings
        Returns:
            Response -- JSON serialized list of ratings
        """
        ratings = Rating.objects.all()

        # Add in the next 3 lines
        rating_game = request.query_params.get('game', None)
        if rating_game is not None:
            ratings = ratings.filter(game_id=rating_game)

        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized rating instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.query_params.get('game', None))
        serializer = CreateRatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer, game=game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a rating
        Returns:
            Response -- Empty body with 204 status code
        """
        rating = Rating.objects.get(pk=pk)
        serializer = CreateRatingSerializer(rating, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        rating = Rating.objects.get(pk=pk)
        rating.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for ratings
    """

    class Meta:
        model = Rating
        fields = (  
                    'id',
                    'gamer',
                    'rating',
                    'game'
                )
        depth = 2

class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'rating',
        )