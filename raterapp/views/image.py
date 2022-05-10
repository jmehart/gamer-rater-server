"""View module for handling requests about ratings"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapp.models.gamer import Gamer
from raterapp.models.image import Image
from raterapp.models.game import Game



class ImageView(ViewSet):
    """Level up images view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single image
        Returns:
            Response -- JSON serialized image
        """
        try:
            image = Image.objects.get(pk=pk)
            serializer = ImageSerializer(image)
            return Response(serializer.data)
        except Image.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all images
        Returns:
            Response -- JSON serialized list of images
        """
        images = Image.objects.all()

        # Add in the next 3 lines
        image_game = request.query_params.get('game', None)
        if image_game is not None:
            images = images.filter(game_id=image_game)

        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized image instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.query_params.get('game', None))
        serializer = CreateImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer, game=game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a image
        Returns:
            Response -- Empty body with 204 status code
        """
        image = Image.objects.get(pk=pk)
        serializer = CreateImageSerializer(image, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        image = Image.objects.get(pk=pk)
        image.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ImageSerializer(serializers.ModelSerializer):
    """JSON serializer for images
    """

    class Meta:
        model = Image
        fields = (  
                    'id',
                    'gamer',
                    'image',
                    'game'
                )
        depth = 2

class CreateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (  
            'image',
        )