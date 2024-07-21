from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider


class APITweetReplies:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_tweet_replies(self):
        """Requests to retrieve user tweets using the configured URL with parameters and headers.

        Returns:
            Response: The response from the API containing user tweets.
        """
        url = f'{self.config["url"]}/tweet/replies?tweet_id=1349129669258448897'
        print(url)
        return self._request.get_request(url, headers=self.config["header"])
