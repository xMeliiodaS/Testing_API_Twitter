import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.api_user_details import APIUserDetails
from logic.api.entities.user_details import UserDetails


class TestAPIUserDetails(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()
        self.user_details = APIUserDetails(self.api_request)

    # ------------------------------------------------------------------------

    def test_get_user_details(self):
        """
        Tests retrieving user details from the API and validating the response.
        """
        # Act
        response = self.user_details.get_user_details(self.config["my_username"],
                                                      self.config["my_user_id"])

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.data['username'], self.config["my_username"])
        self.assertEqual(response.data['user_id'], self.config["my_user_id"])

    # ------------------------------------------------------------------------

    def test_post_user_details(self):
        """
        Tests posting user details to the API and validating the response.
        """
        # Arrange
        user_details_body = UserDetails(self.config["my_username"], self.config["my_user_id"])

        # Act
        response = self.user_details.post_user_details(user_details_body.to_dict())

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(self.config["my_username"], response.data["username"])

    # ------------------------------------------------------------------------

    def test_post_user_details_incorrect(self):
        """
        Tests posting user details to the API and validating the response.
        """
        # Arrange
        user_details_body = UserDetails(self.config["my_username"], self.config["my_user_id"])

        # Act
        response = self.user_details.post_user_details(user_details_body.to_dict())

        # Assert
        self.assertTrue(response.ok)
        self.assertNotEqual(self.config["incorrect_username"], response.data["username"])
