import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.api_tweet_details import APITweetDetails
from logic.api.entities.tweet_details import TweetDetails


class TestAPITweetDetails(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

    def test_get_tweet_details(self):
        """
        Tests retrieving tweet details from the API and validating the response.
        """
        tweet_details = APITweetDetails(self.api_request)
        response = tweet_details.get_tweet_details()
        user_body = response.json()
        user = user_body["user"]

        self.assertTrue(response.ok)
        self.assertEqual(self.config['tweet_id'], user_body['tweet_id'])
        self.assertEqual(self.config["username"], user['username'])

    def test_post_tweet_details(self):
        """
        Tests retrieving tweet details from the API and validating the response.
        """
        tweet = TweetDetails(self.config["tweet_id"])
        tweet_details = APITweetDetails(self.api_request)
        response = tweet_details.post_tweet_details(tweet.to_dict())
        user_body = response.json()
        user = user_body["user"]

        self.assertTrue(response.ok)
        self.assertEqual(self.config['tweet_id'], user_body['tweet_id'])
        self.assertEqual(self.config["username"], user['username'])
