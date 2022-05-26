from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from raterapp.models import Gamer
from raterapp.models.rating import Rating
from raterapp.views.rating import CreateRatingSerializer, RatingSerializer

class RatingTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'gamers', 'category', 'games', 'images', 'reviews', 'ratings']

    def setUp(self):
        # Grab the first Gamer object from the database and add their token to the headers
        self.gamer = Gamer.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_rating(self):
        """Create rating test"""
        url = "/ratings?game=1"

        # Define the Game properties
        # The keys should match what the create method is expecting
        # Make sure this matches the code you have
        rating = {
            "rating": 1
        }

        response = self.client.post(url, rating, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        # Get the last rating added to the database, it should be the one just created
        new_rating = Rating.objects.last()

        expected = CreateRatingSerializer(new_rating)

        # Now we can test that the expected output matches what was actually returned
        self.assertEqual(expected.data, response.data)

    def test_change_rating(self):
        """test update rating"""
        # Grab the first rating in the database
        rating = Rating.objects.first()

        url = f'/ratings/{rating.id}'

        updated_rating = {
            "rating": rating.rating + 1
        }

        response = self.client.put(url, updated_rating, format='json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        # Refresh the rating object to reflect any changes in the database
        rating.refresh_from_db()

        # assert that the updated value matches
        self.assertEqual(updated_rating['rating'], rating.rating)