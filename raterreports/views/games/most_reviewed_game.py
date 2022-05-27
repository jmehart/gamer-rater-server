"""Module for generating top 5 games report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterreports.views.helpers import dict_fetch_all

class MostReviewedGameList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
                SELECT
                    *
                FROM (
                    SELECT
                        g.*,
                        COUNT(r.id) AS Reviews
                    FROM raterapp_game g
                    LEFT JOIN raterapp_review r
                        ON r.game_id = g.id
                    GROUP BY g.id
                )
                WHERE Reviews = (
                    SELECT
                        MAX(Reviews)
                    FROM (
                        SELECT
                            g.*,
                            COUNT(r.id) AS Reviews
                        FROM raterapp_game g
                        LEFT JOIN raterapp_review r
                            ON r.game_id = g.id
                        GROUP BY g.id
                    )
                )
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            most_reviewed_games = []

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
                    "reviews": row['Reviews']
                }
                most_reviewed_games.append(game)
        
        # The template string must match the file name of the html template
        template = 'games/list_most_reviewed_game.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "most_reviewed_games_list": most_reviewed_games
        }

        return render(request, template, context)