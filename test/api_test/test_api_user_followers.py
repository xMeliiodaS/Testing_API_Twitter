import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.api_user_followers import APIUserFollowers


class TestAPIUserFollowers(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

    def test_get_user_tweets(self):
        user_details = APIUserFollowers(self.api_request)
        response = user_details.get_user_followers()
        response_body = response.json()

        self.assertTrue(response.ok)

        followers = response_body["results"]
        self.assertEqual(followers[1]["user_id"], self.config["follower_user_id"])
        self.assertEqual(followers[1]["username"], self.config["follower_user_name"])
