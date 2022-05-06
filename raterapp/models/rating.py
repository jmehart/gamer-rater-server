from django.db import models


class Rating(models.Model):
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    rating = models.CharField(max_length=55)