from django.db import models


class Review(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=55)