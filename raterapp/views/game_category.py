from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapp.models import GameCategory


class GameCategoryView(ViewSet):
    """Level up game types"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            game_category = GameCategory.objects.get(pk=pk)
            serializer = GameCategorySerializer(game_category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all game categories
        Returns:
            Response -- JSON serialized list of game categories
        """
        game_categories = GameCategory.objects.all()

        # Note the additional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.
        serializer = GameCategorySerializer(
            game_categories, many=True, context={'request': request})
        return Response(serializer.data)

class GameCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for game categories
    Arguments:
        serializers
    """
    class Meta:
        model = GameCategory
        fields = ('id', 'category', 'game')
        depth = 1