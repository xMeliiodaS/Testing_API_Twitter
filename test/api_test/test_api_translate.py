import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.api_user_media import APIUserMedia
from logic.api.entities.user_media import UserMedia


class TestAPITweetDetails(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by initializing APIWrapper and loading configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_config_json()

    def test_get_user_media(self):
        api_user_media = APIUserMedia(self.api_request)
        response = api_user_media.get_user_media()
        response_body = response.json()

        user_media_list = response_body["results"][0]

        self.assertTrue(response.ok)
        self.assertEqual(self.config["user_id"], user_media_list["user"]["user_id"])

    def test_post_user_media(self):
        """
        Tests posting translate from the API and validating the response.
        """
        user_media = UserMedia("96479162", 10)
        api_user_media = APIUserMedia(self.api_request)
        response = api_user_media.post_user_media(user_media.to_dict())
        response_body = response.json()

        user_media_list = response_body["results"][0]

        self.assertTrue(response.ok)
        self.assertEqual(self.config["user_id"], user_media_list["user"]["user_id"])