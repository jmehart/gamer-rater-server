"""Module for generating games in category count report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterreports.views.helpers import dict_fetch_all

class Top3ReviewersList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
                SELECT
                    gr.*,
                    u.first_name || " " || u.last_name AS full_name,
                    COUNT(r.gamer_id) AS review_count
                FROM raterapp_gamer gr
                LEFT JOIN raterapp_review r
                    ON gr.id = r.gamer_id
                JOIN auth_user u
                    ON gr.id = u.id
                GROUP BY gr.id
                ORDER BY review_count DESC
                LIMIT 3
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            top_3_game_reviewers = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the name, description, number_of_players, maker,
                # game_type_id, and skill_level from the row dictionary
                gamer = {
                    "id": row['id'],
                    "full_name": row['full_name'],
                    "review_count": row['review_count'],
                    "bio": row['bio']
                }
                top_3_game_reviewers.append(gamer)
        
        # The template string must match the file name of the html template
        template = 'gamers/list_top_3_game_reviewers.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "top_3_game_reviewers_list": top_3_game_reviewers
        }

        return render(request, template, context)