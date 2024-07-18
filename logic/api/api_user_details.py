import json

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider


class APIUserDetails:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_details(self):
        """Requests to shuffle the deck with a specified number of decks.

        Args:
            url (str): The base URL of the API.
            headers (dict): The headers to include in the request.

        Returns:
            Response: The response from the API.
        """
        url = (f"{self.config['url']}/{self.config['end_url_details']}"
               f"?username={self.config['username']}&user_id={self.config['user_id']}")
        return self._request.get_request(url, headers=self.config["header"])

    def post_user_details(self, user_name_details):
        return self._request.post_request(f'{self.config["url"]}/user/details', self.config["header"],
                                          user_name_details)

    # def post_user_details(self, user_name_details):
    #     # return self._request.post_request(f'{self.config["url"]}/user/details', self.config["header"],
    #     #                                  json.dumps(user_name_details))
    #     response = self._request.post_request(f'{self.config["url"]}/user/details', self.config["header"],
    #                                           json.dumps(user_name_details))
    #     response_wrapper = ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
    #     return response_wrapper
