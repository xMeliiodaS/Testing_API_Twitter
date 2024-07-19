from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider


class APIUserTweets:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_tweets_by_url(self):
        """Requests to retrieve user tweets using the configured URL with parameters and headers.

        Returns:
            Response: The response from the API containing user tweets.
        """
        url = (f"{self.config['url']}/{self.config['end_url_tweets']}"
               f"?username={self.config['username']}&limit=40&user_id={self.config['user_id']}"
               f"&include_replies=false&include_pinned=false")
        return self._request.get_request(url, headers=self.config["header"])
