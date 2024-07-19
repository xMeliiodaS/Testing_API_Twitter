import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.api_user_tweets import APIUserTweets


class TestAPIUserTweets(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

    def test_get_user_details(self):
        """
        Tests the retrieval of user tweets by calling the API and validating the response.
        """
        user_details = APIUserTweets(self.api_request)
        response = user_details.get_user_tweets_by_url()
        response_body = response.json()

        self.assertTrue(response.ok)

        first_tweet = response_body["results"][0]
        self.assertIn("tweet_id", first_tweet)
        self.assertEqual(first_tweet["tweet_id"], self.config["tweet_id"])

        # Check the structure of the user object in the first tweet
        user_info = first_tweet["user"]
        self.assertEqual(user_info["username"], self.config["username"])
