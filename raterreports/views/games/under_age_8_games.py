"""Module for generating games in category count report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterreports.views.helpers import dict_fetch_all

class GamesUnderAge8List(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
                SELECT *
                FROM raterapp_game g
                WHERE g.age < 8
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            games_under_age_8 = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the name, description, number_of_players, maker,
                # game_type_id, and skill_level from the row dictionary
                game = {
                    "id": row['id'],
                    "title": row['title'],
                    "description": row['description'],
                    "designer": row['designer'],
                    "year_released": row['year_released'],
                    "estimated_time": row['estimated_time'],
                    "num_of_players": row['num_of_players'],
                    "age": row['age'],
                    "gamer_id": row['gamer_id']
                }
                games_under_age_8.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/list_under_age_8_games.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "under_age_8_games_list": games_under_age_8
        }

        return render(request, template, context)