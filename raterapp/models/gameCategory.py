from django.db import models


class GameCategory(models.Model):
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    categoryId = models.ForeignKey("Category", on_delete=models.CASCADE)