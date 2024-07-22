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

    def test_get_user_details(self):
        """
        Tests retrieving user details from the API and validating the response.
        """
        user_details = APIUserDetails(self.api_request)
        response = user_details.get_user_details(self.config["my_username"], self.config["my_user_id"])
        response_body = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(response_body['username'], self.config["my_username"])
        self.assertEqual(response_body['user_id'], self.config["my_user_id"])

    def test_post_user_details(self):
        """
        Tests posting user details to the API and validating the response.
        """
        user_details = APIUserDetails(self.api_request)
        user_details_body = UserDetails(self.config["my_username"], self.config["my_user_id"])

        response = user_details.post_user_details(user_details_body.to_dict())
        response_body = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(self.config["my_username"], response_body["username"])

    def test_post_user_details_incorrect(self):
        """
        Tests posting user details to the API and validating the response.
        """
        user_details = APIUserDetails(self.api_request)
        user_details_body = UserDetails(self.config["my_username"], self.config["my_user_id"])

        response = user_details.post_user_details(user_details_body.to_dict())
        response_body = response.json()

        self.assertTrue(response.ok)
        self.assertNotEqual(self.config["incorrect_username"], response_body["username"])
