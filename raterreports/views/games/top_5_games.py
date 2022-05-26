"""Module for generating top 5 games report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterreports.views.helpers import dict_fetch_all

class Top5GameList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
                SELECT
                    g.*,
                    CASE WHEN AVG(r.rating) ISNULL THEN 0 ELSE AVG(r.rating) END AS Rating
                FROM raterapp_game g
                LEFT JOIN raterapp_rating r
                    ON r.game_id = g.id
                GROUP BY g.id
                ORDER BY rating DESC
                LIMIT 5
                
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            top_5_games = []

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
                    "gamer_id": row['gamer_id'],
                    "rating": row['Rating'],
                }
                top_5_games.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/list_top_5_games.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "top5games_list": top_5_games
        }

        return render(request, template, context)