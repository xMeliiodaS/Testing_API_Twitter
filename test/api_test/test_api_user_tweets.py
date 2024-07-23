import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.api_user_tweets import APIUserTweets
from logic.api.utils import Utils


class TestAPIUserTweets(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

    # ------------------------------------------------------------------------

    def test_get_user_tweets(self):
        """
        Tests the retrieval of user tweets by calling the API and validating the response.
        """

        # Act
        user_tweets = APIUserTweets(self.api_request)
        response = user_tweets.get_user_tweets_by_url(self.config["my_username"],
                                                      self.config["limit"],
                                                      self.config["my_user_id"],
                                                      self.config["include_replies"],
                                                      self.config["include_pinned"])

        tweets = response.data["results"]
        found_tweet = Utils.find_tweet_by_id(tweets, self.config["my_first_tweet_id"])

        # Assert
        self.assertTrue(response.ok)

        self.assertEqual(found_tweet["tweet_id"], self.config["my_first_tweet_id"])

        # Extract the list of users from the first tweet
        user_info = found_tweet["user"]
        self.assertEqual(user_info["username"], self.config["my_username"])
