from infra.browser.configure_provider import ConfigProvider


class APITweetDetails:
    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_tweet_details(self, tweet_id):
        """
        Retrieve tweet details using the configured URL with parameters and headers.
        tweet_id (str): The ID of the tweet to retrieve.
        Returns: The response from the API containing tweet details.
        """
        url = f"{self.config['url']}/{self.config['tweet_details_endpoint']}?tweet_id={tweet_id}"
        return self._request.get_request(url, headers=self.config["header"])

    def post_tweet_details(self, follower_details):
        """
        Post follower details to the tweet details endpoint.
        follower_details (dict): The details of the follower to post.
        Returns: The response from the API after posting the follower details.
        """
        return self._request.post_request(f'{self.config["url"]}/{self.config["tweet_details_endpoint"]}',
                                          self.config["header"], follower_details)
