import json

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider


class APIUserDetails:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_details(self):
        """Requests to retrieve user details using the configured URL and headers.

        Returns:
            Response: The response from the API containing user details.
        """
        url = (f"{self.config['url']}/{self.config['end_url_details']}"
               f"?username={self.config['username']}&user_id={self.config['user_id']}")
        return self._request.get_request(url, headers=self.config["header"])

    def post_user_details(self, user_name_details):
        """Sends a POST request to update user details.

            user_name_details (dict): The user details to be updated.

        Returns:
            Response: The response from the API.
        """
        return self._request.post_request(f'{self.config["url"]}/user/details', self.config["header"],
                                          user_name_details)
