import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.api_user_followers import APIUserFollowers
from logic.api.entities.user_follower import UserFollower


class TestAPIUserFollowers(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()
        self.user_details = APIUserFollowers(self.api_request)

    def test_get_user_followers(self):
        """
        Tests getting user followers to the API and validating the responses.
        """
        response = self.user_details.get_user_followers()
        response_body = response.json()

        self.assertTrue(response.ok)

        followers = response_body["results"]
        self.assertEqual(followers[1]["user_id"], self.config["follower_user_id"])
        self.assertEqual(followers[1]["username"], self.config["follower_user_name"])

    def test_post_user_follower(self):
        """
        Tests posting user followers to the API and validating the responses.
        """
        user_follower = UserFollower(self.config["user_id"],
                                     self.config["limit"])
        response = self.user_details.post_user_followers(user_follower.to_dict())
        response_body = response.json()

        # Extract the list of followers from the response body
        followers = response_body["results"]
        self.assertTrue(response.ok)
        self.assertEqual(self.config["follower_user_id"], followers[1]["user_id"])