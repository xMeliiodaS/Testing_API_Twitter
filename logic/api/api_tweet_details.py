from infra.browser.configure_provider import ConfigProvider
from logic.api.entities.tweet_details import TweetDetails


class APITweetDetails:
    ENDPOINT = "/tweet/details?"

    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_tweet_details(self, tweet_id):
        """
        Retrieve tweet details using the configured URL with parameters and headers.
        tweet_id (str): The ID of the tweet to retrieve.
        Returns: The response from the API containing tweet details.
        """
        tweet_detail_param = TweetDetails(tweet_id).__str__()
        url = f"{self.config['url']}{self.ENDPOINT}{tweet_detail_param}"
        return self._request.get_request(url, headers=self.config["header"])

    def post_tweet_details(self, follower_details):
        """
        Post follower details to the tweet details endpoint.
        follower_details (dict): The details of the follower to post.
        Returns: The response from the API after posting the follower details.
        """
        return self._request.post_request(f'{self.config["url"]}{self.ENDPOINT}',
                                          self.config["header"], follower_details)
