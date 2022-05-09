from django.db import models

class Game(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    description = models.TextField()
    designer = models.CharField(max_length=55)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    estimated_time = models.IntegerField()
    age = models.IntegerField()
    categories = models.ManyToManyField("Category",
                                    through="GameCategory",
                                    related_name="games")