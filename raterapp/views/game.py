"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapp.models.game import Game
from raterapp.models.gamer import Gamer
from raterapp.models.review import Review
from raterapp.models.rating import Rating
from raterapp.models.game_category import GameCategory



class GameView(ViewSet):
    """GamerRater game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games
        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()

        # Add in the next 3 lines
        # game_category = request.query_params.get('category', None)
        # if game_category is not None:
        #     games = games.filter(game_type_id=game_category)

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer)
        game = Game.objects.get(pk=serializer.data["id"])
        game.categories.add(*request.data["categories"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        game = Game.objects.get(pk=pk)
        serializer = CreateGameSerializer(game, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # game_categories = GameCategory.objects.filter(game_id=pk)
        game.categories.remove(*game.categories.all())
        game.categories.add(*request.data["categories"])

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'game_id', 'gamer_id', 'review')

class GameRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'game_id', 'gamer_id', 'rating')

class GameCategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = GameCategory
        fields = ('id', 'cat_id', 'game_id')
        depth = 1

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    Arguments:
        serializer type
    """
    ratings = GameRatingSerializer
    reviews = GameReviewSerializer(many=True)
    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'designer', 'year_released', 'num_of_players', 'estimated_time', 'age', 'gamer', 'categories', 'reviews']
        depth: 2
        
class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game       
        fields = ['id', 'title', 'description', 'designer', 'year_released', 'num_of_players', 'estimated_time', 'age'] 