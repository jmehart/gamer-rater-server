from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from raterapp.models import Game, Gamer
from raterapp.views.game import CreateGameSerializer, GameSerializer

class GameTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'gamers', 'category', 'games', 'images', 'reviews', 'ratings']

    def setUp(self):
        # Grab the first Gamer object from the database and add their token to the headers
        self.gamer = Gamer.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_list_games(self):
        """Test list games"""
        url = '/games'

        response = self.client.get(url)

        # Get all the games in the database and serialize them to get the expected output
        all_games = Game.objects.all()
        expected = GameSerializer(all_games, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(expected.data, response.data)

    def test_create_game(self):
        """Create game test"""
        url = "/games"

        # Define the Game properties
        # The keys should match what the create method is expecting
        # Make sure this matches the code you have
        game = {
            "title": "Clue",
            "description": "It was Prof. Plum",
            "designer": "Milton Bradley",
            "year_released": 1940,
            "num_of_players": 4,
            "estimated_time": 60,
            "age": 5,
            "categories": [1, 2]
        }

        response = self.client.post(url, game, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        # Get the last game added to the database, it should be the one just created
        new_game = Game.objects.last()

        expected = CreateGameSerializer(new_game)

        # Now we can test that the expected output matches what was actually returned
        self.assertEqual(expected.data, response.data)

    def test_get_game(self):
        """Get Game Test
        """
        # Grab a game object from the database
        game = Game.objects.first()

        url = f'/games/{game.id}'

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        # Like before, run the game through the serializer that's being used in view
        expected = GameSerializer(game)

        # Assert that the response matches the expected return data
        self.assertEqual(expected.data, response.data)

    def test_change_game(self):
        """test update game"""
        # Grab the first game in the database
        game = Game.objects.first()

        url = f'/games/{game.id}'

        updated_game = {
            "title": f'{game.title} updated',
            "description": game.description,
            "designer": game.designer,
            "year_released": game.year_released,
            "num_of_players": game.num_of_players,
            "estimated_time": game.estimated_time,
            "age": game.age,
            "categories": [2, 3]
        }

        response = self.client.put(url, updated_game, format='json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        # Refresh the game object to reflect any changes in the database
        game.refresh_from_db()

        # assert that the updated value matches
        self.assertEqual(updated_game['title'], game.title)

    def test_delete_game(self):
        """Test delete game"""
        game = Game.objects.first()

        url = f'/games/{game.id}'
        response = self.client.delete(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        # Test that it was deleted by trying to _get_ the game
        # The response should return a 404
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)