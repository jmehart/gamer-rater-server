"""View module for handling requests about game types"""
from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapp.models import Gamer


class GamerView(ViewSet):
    
    def list(self, request):
        gamer = Gamer.objects.get(user=request.auth.user)
        
        serializer = GamerSerializer(gamer)
        return Response(serializer.data)

class GamerSerializer(serializers.ModelSerializer):
    """JSON serializer for gamers"""
    class Meta:
        model = Gamer
        fields = ('id', 'user_id')
        depth = 1