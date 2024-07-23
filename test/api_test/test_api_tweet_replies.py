import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.api_tweet_replies import APITweetReplies
from logic.api.utils import Utils


class TestAPITweetReplies(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

    # ------------------------------------------------------------------------

    def test_get_tweet_replies(self):
        """
        Tests retrieving tweet details from the API and validating the response.
        """
        # Arrange
        tweet_replies = APITweetReplies(self.api_request)

        # Act
        response = tweet_replies.get_tweet_replies(self.config["tweet_reply_id"])

        # Extract the list of tweets from the response body
        tweets = response.data["replies"]

        # Use the helper function to find the tweet
        found_tweet = Utils.find_tweet_by_id(tweets, self.config["replied_tweet_id"])

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(self.config["replied_tweet_id"], found_tweet["tweet_id"])
