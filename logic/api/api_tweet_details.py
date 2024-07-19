from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider


class APITweetDetails:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_tweet_details(self):
        """
        Requests to retrieve tweet details using the configured URL with parameters and headers.

        Returns:
            Response: The response from the API containing tweet details.
        """
        url = f"{self.config['url']}/tweet/details?tweet_id={self.config['tweet_id']}"
        return self._request.get_request(url, headers=self.config["header"])

    def post_tweet_details(self, follower_details):
        return self._request.post_request(f'{self.config["url"]}/tweet/details',
                                          self.config["header"], follower_details)
