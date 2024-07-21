import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.api_tweet_replies import APITweetReplies


class TestAPITweetReplies(unittest.TestCase):

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
        tweet_replies = APITweetReplies(self.api_request)
        response = tweet_replies.get_tweet_replies()
        response_body = response.json()

        print(response_body)
