from django.urls import path

from .views import Top5GameList, Bottom5GameList, CategoryGameCountList, GreaterThan5PlayersGameList, MostReviewedGameList, MostGamesAddedByGamerList, GamesUnderAge8List, NoImageGamesList, Top3ReviewersList 

urlpatterns = [
    path('reports/top5games', Top5GameList.as_view()),
    path('reports/bottom5games', Bottom5GameList.as_view()),
    path('reports/gamesbycategory', CategoryGameCountList.as_view()),
    path('reports/gamesgreaterthan5players', GreaterThan5PlayersGameList.as_view()),
    path('reports/mostreviewedgame', MostReviewedGameList.as_view()),
    path('reports/mostgamesaddedbygamer', MostGamesAddedByGamerList.as_view()),
    path('reports/underage8games', GamesUnderAge8List.as_view()),
    path('reports/noimagegames', NoImageGamesList.as_view()),
    path('reports/top3reviewers', Top3ReviewersList.as_view()),
]