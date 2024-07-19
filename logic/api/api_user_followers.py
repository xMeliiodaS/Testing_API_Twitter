from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider


class APIUserFollowers:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_followers(self):
        """Requests to retrieve user tweets using the configured URL with parameters and headers.

        Returns:
            Response: The response from the API containing user tweets.
        """
        url = (f"{self.config['url']}/{self.config['end_url_followers']}"
               f"?user_id={self.config['user_id']}&limit=10")
        return self._request.get_request(url, headers=self.config["header"])
