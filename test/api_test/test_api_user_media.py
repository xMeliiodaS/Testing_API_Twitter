import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.api_user_media import APIUserMedia
from logic.api.entities.user_media import UserMedia
from logic.api.utils import Utils


class TestAPITweetDetails(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()
        self.api_user_media = APIUserMedia(self.api_request)

    # ------------------------------------------------------------------------

    def test_get_user_media(self):
        """
        Tests getting user media from the API and validating the response.
        """
        # Act
        response = self.api_user_media.get_user_media(self.config["my_user_id"], self.config["limit"])
        user_media_list = response.data["results"]
        found_media = Utils.find_user_media_by_user_id(user_media_list,
                                                       self.config["my_user_id"])

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(self.config["my_user_id"], found_media["user"]["user_id"])
        self.assertEqual(self.config["my_username"], found_media["user"]["username"])

    # ------------------------------------------------------------------------

    def test_get_user_media_incorrect(self):
        """
        Tests retrieving user medias from the API and validating the wrong data.
        """
        # Act
        response = self.api_user_media.get_user_media(self.config["my_user_id"], self.config["limit"])
        user_media_list = response.data["results"]
        found_media = Utils.find_user_media_by_user_id(user_media_list,
                                                       self.config["my_user_id"])

        # Assert
        self.assertTrue(response.ok)
        self.assertNotEqual(self.config["incorrect_user_id"], found_media["user"]["user_id"])
        self.assertNotEqual(self.config["incorrect_username"], found_media["user"]["username"])

    # ------------------------------------------------------------------------

    def test_post_user_media(self):
        """
        Tests posting user media from the API and validating the response.
        """
        # Arrange
        user_media = UserMedia(self.config["my_user_id"], self.config["limit"])

        # Act
        response = self.api_user_media.post_user_media(user_media.to_dict())
        user_media_list = response.data["results"]
        found_media = Utils.find_user_media_by_user_id(user_media_list,
                                                       self.config["my_user_id"])

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(self.config["my_user_id"], found_media["user"]["user_id"])
        self.assertEqual(self.config["my_username"], found_media["user"]["username"])
