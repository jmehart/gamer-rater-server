"""Module for generating games in category count report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from raterreports.views.helpers import dict_fetch_all

class CategoryGameCountList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            # TODO: Write a query to get all games along with the gamer first name, last name, and id
            db_cursor.execute("""
                SELECT 
                    c.id,
                    c.type,
                    COUNT(gc.category_id) AS game_count
                FROM raterapp_category c
                LEFT JOIN raterapp_gamecategory gc
                    ON gc.category_id = c.id
                GROUP BY c.id
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            category_game_count = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the name, description, number_of_players, maker,
                # game_type_id, and skill_level from the row dictionary
                count = {
                    "id": row['id'],
                    "type": row['type'],
                    "game_count": row['game_count']
                }
                category_game_count.append(count)
        
        # The template string must match the file name of the html template
        template = 'games/list_games_by_category.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "cat_games_count_list": category_game_count
        }

        return render(request, template, context)