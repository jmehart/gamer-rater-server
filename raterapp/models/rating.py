from django.db import models


class Rating(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()