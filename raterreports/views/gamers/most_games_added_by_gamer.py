"""Module for generating games in category count report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterreports.views.helpers import dict_fetch_all

class MostGamesAddedByGamerList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
                SELECT *
                FROM (
                        SELECT
                            gr.*,
                            u.first_name || " " || u.last_name AS full_name,
                            COUNT(g.gamer_id) AS games_added
                        FROM raterapp_gamer gr
                        LEFT JOIN raterapp_game g
                            ON gr.id = g.gamer_id
                        JOIN auth_user u
                            ON gr.id = u.id
                        GROUP BY gr.id
                )
                WHERE games_added = (
                    SELECT
                        MAX(games_added)
                    FROM (
                        SELECT
                            gr.*,
                            COUNT(g.gamer_id) AS games_added
                        FROM raterapp_gamer gr
                        LEFT JOIN raterapp_game g
                            ON gr.id = g.gamer_id
                        GROUP BY gr.id
                    )
                )
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            gamers_most_games_added = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the name, description, number_of_players, maker,
                # game_type_id, and skill_level from the row dictionary
                gamer = {
                    "id": row['id'],
                    "full_name": row['full_name'],
                    "games_added": row['games_added'],
                    "bio": row['bio']
                }
                gamers_most_games_added.append(gamer)
        
        # The template string must match the file name of the html template
        template = 'gamers/list_most_games_added_by_gamer.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "most_games_added_by_gamer_list": gamers_most_games_added
        }

        return render(request, template, context)