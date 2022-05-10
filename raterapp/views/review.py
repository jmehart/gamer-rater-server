"""View module for handling requests about reviews"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapp.models.gamer import Gamer
from raterapp.models.game import Game
from raterapp.models.review import Review


class ReviewView(ViewSet):
    """Level up reviews view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single review
        Returns:
            Response -- JSON serialized review
        """
        try:
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all reviews
        Returns:
            Response -- JSON serialized list of reviews
        """
        reviews = Review.objects.all()

        # Add in the next 3 lines
        review_game = request.query_params.get('game', None)
        if review_game is not None:
            reviews = reviews.filter(game_id=review_game)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized review instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.query_params.get('game', None))
        serializer = CreateReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer, game=game)
        #serializer.save(game=game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a review
        Returns:
            Response -- Empty body with 204 status code
        """
        review = Review.objects.get(pk=pk)
        serializer = CreateReviewSerializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    """

    class Meta:
        model = Review
        fields = (
                    'id',
                    'review',
                    'game',
                    'gamer'
                )
        depth = 2

class CreateReviewSerializer(serializers.ModelSerializer):
    
    #game = Game.objects.get(pk=data["game_id"])
    
    class Meta:
        model = Review
        fields = (
            'review',
        )