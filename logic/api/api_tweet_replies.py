from infra.browser.configure_provider import ConfigProvider


class APITweetReplies:
    ENDPOINT = 'tweet/replies'

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
                                         f'{self.ENDPOINT}?tweet_id={tweet_id}',
                                         headers=self.config["header"])

    @staticmethod
    def find_tweet_by_id(tweets, tweet_id):
        """
        Finds a tweet by its ID in a list of tweets.

        Args:
            tweets (list): The list of tweets to search through.
            tweet_id (str): The ID of the tweet to find.

        Returns:
            dict: The tweet with the matching ID, or None if not found.
        """
        for tweet in tweets:
            if tweet["tweet_id"] == tweet_id:
                return tweet
        return None
