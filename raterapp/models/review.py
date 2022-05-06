from django.db import models


class Review(models.Model):
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    review = models.CharField(max_length=55)