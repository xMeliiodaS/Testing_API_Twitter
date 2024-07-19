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
        user = user_details.get_user_details()
        user_body = user.json()

        self.assertTrue(user.ok)
        self.assertEqual(user_body['username'], self.config["username"])
        self.assertEqual(user_body['user_id'], self.config["user_id"])

    def test_post_user_details(self):
        """
        Tests posting user details to the API and validating the response.
        """
        user_details = APIUserDetails(self.api_request)
        user_details_body = UserDetails(self.config["username_post"], self.config["user_id_post"])

        user_response = user_details.post_user_details(user_details_body.to_dict())
        user_body = user_response.json()

        self.assertTrue(user_response.ok)
        self.assertEqual(user_response.status_code, 200)
        self.assertEqual(self.config["username_post"], user_body["username"])
