from django.urls import path

from .views import Top5GameList, Bottom5GameList, CategoryGameCountList, GreaterThan5PlayersGameList

urlpatterns = [
    path('reports/top5games', Top5GameList.as_view()),
    path('reports/bottom5games', Bottom5GameList.as_view()),
    path('reports/gamesbycategory', CategoryGameCountList.as_view()),
    path('reports/gamesgreaterthan5players', GreaterThan5PlayersGameList.as_view()),
]