import unittest

from parameterized import parameterized

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

    @parameterized.expand([
        ["1651463042331230208", "1651463042331230208"],
        ["1814982968110194714", "1814982968110194714"]
    ])
    def test_get_tweet_details(self, tweet_id, expected_tweet_id):
        """
        Tests retrieving tweet details from the API and validating the response.
        """
        tweet_details = APITweetDetails(self.api_request)
        response = tweet_details.get_tweet_details(tweet_id)
        user_body = response.json()

        # Extract the list of users from the response body
        user = user_body["user"]

        self.assertTrue(response.ok)
        self.assertEqual(expected_tweet_id, user_body['tweet_id'])
        self.assertEqual(self.config["my_username"], user['username'])

    @parameterized.expand([
        ["1651463042331230208", "8567456774575674374"],
        ["1814982968110194714", "3645735466772864383"]
    ])
    def test_get_tweet_details_incorrect_data(self, tweet_id, expected_tweet_id):
        """
        Tests retrieving tweet details from the API and validating the wrong data.
        """
        tweet_details = APITweetDetails(self.api_request)
        response = tweet_details.get_tweet_details(tweet_id)
        user_body = response.json()

        self.assertNotEquals(expected_tweet_id, user_body['tweet_id'])

    def test_post_tweet_details(self):
        """
        Tests retrieving tweet details from the API and validating the response.
        """
        tweet = TweetDetails(self.config["my_tweet_id"])
        tweet_details = APITweetDetails(self.api_request)
        response = tweet_details.post_tweet_details(tweet.to_dict())
        user_body = response.json()

        # Extract the list of users from the response body
        user = user_body["user"]

        self.assertTrue(response.ok)
        self.assertEqual(self.config['my_tweet_id'], user_body['tweet_id'])
        self.assertEqual(self.config["my_username"], user['username'])


if __name__ == '__main__':
    unittest.main()
