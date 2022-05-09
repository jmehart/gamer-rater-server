"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from raterapp.models.category import Category


class CategoryView(ViewSet):

    def retrieve(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = GameSerializer(category)
        return Response(serializer.data)

    def list(self, request):
        categories = Category.objects.all()
        serializer = GameSerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized game instance
        """
        
        try:
            serializer = GameSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'type']