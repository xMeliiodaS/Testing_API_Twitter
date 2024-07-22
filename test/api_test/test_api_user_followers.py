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

    # ------------------------------------------------------------------------

    def test_user_followers_by_url(self):
        """
        Tests getting user followers to the API and validating the responses.
        """
        # Act
        response = self.user_details.get_user_followers(self.config["follower_user_id"], self.config["limit"])

        # Assert
        self.assertTrue(response.ok)
        print(response.data)
        followers = response.data["results"]
        self.assertEqual(followers[1]["user_id"], self.config["actual_user_id"])
        self.assertEqual(followers[1]["username"], self.config["actual_follower_username"])

    # ------------------------------------------------------------------------

    def test_user_follower_by_body(self):
        """
        Tests user followers to the API and validating the responses.
        """
        # Arrange
        user_follower = UserFollower(self.config["my_user_id"],
                                     self.config["limit"])

        # Act
        response = self.user_details.post_user_followers(user_follower.to_dict())

        followers = response.data["results"]

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(self.config["my_follower_id"], followers[0]["user_id"])
        self.assertEqual(self.config["my_follower_username"], followers[0]["username"])
