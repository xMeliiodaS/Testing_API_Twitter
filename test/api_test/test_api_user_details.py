import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.user_details import UserDetails


class TestAPIShuffleCard(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()

        self.username = self.config["username"]
        self.user_id = self.config["user_id"]

    def test_shuffle_the_cards(self):
        """
        Tests the shuffling of the deck by calling the API and validating the response.
        """
        user_details = UserDetails(self.api_request)
        user = user_details.get_user_details(self.config["url"], self.config["header"], self.username, self.user_id)
        user_body = user.json()
        print(user_body)

        self.assertTrue(user.ok)
        self.assertEqual(user_body['username'], self.username)
        self.assertEqual(user_body['user_id'], self.user_id)

