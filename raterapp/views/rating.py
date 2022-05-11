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
    """Gamer Rater games"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized game instance
        """

        gamer = Gamer.objects.get(user=request.auth.user)
        game= Game.objects.get(pk=request.data['game'])
        try:
            rating = Rating.objects.create(
                rating=request.data['rating'],
                gamer=gamer,
                game=game
            )
            serializer = RatingSerializer(rating, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        ratings = Rating.objects.all()

        serializer = RatingSerializer(
            ratings, many=True, context={'request': request})
        return Response(serializer.data)
        

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'gamer', 'game', 'rating')
        depth = 1