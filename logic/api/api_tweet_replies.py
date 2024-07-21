from infra.browser.configure_provider import ConfigProvider


class APITweetReplies:
    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_tweet_replies(self, tweet_id):
        """
        Retrieve user tweets using the configured URL with parameters and headers.
        tweet_id (str): The ID of the tweet to get replies for.
        Returns: The response from the API containing user tweets.
        """
        return self._request.get_request(f'{self.config["url"]}/'
                                         f'{self.config["tweet_replies_endpoint"]}?tweet_id={tweet_id}',
                                         headers=self.config["header"])
