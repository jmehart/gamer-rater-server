from django.db import models


class Image(models.Model):
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    image = models.CharField(max_length=55)