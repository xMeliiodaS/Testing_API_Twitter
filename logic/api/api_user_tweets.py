from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider


class APIUserTweets:
    ENDPOINT = '/user/tweets'
    USERNAME_PARAM = '?username='
    USER_ID_PARAM = '&user_id='
    LIMIT = '&limit='
    INCLUDE_REPLIES = '&include_replies='
    INCLUDE_PINNED = '&include_pinned='

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_tweets_by_url(self, username, limit, user_id, include_replies, include_pinned):
        """
        Send a GET request to retrieve user tweets.
        username (str): The username of the user.
        limit (int): The maximum number of tweets to retrieve.
        user_id (str): The ID of the user.
        include_replies (bool): Whether to include replies.
        include_pinned (bool): Whether to include pinned tweets.
        Returns: The response from the API containing user tweets.
        """
        url = (f"{self.config['url']}{self.ENDPOINT}"
               f"{self.USERNAME_PARAM}{username}{self.LIMIT}{limit}{self.USER_ID_PARAM}{user_id}"
               f"{self.INCLUDE_REPLIES}{include_replies}{self.INCLUDE_PINNED}{include_pinned}")
        return self._request.get_request(url, headers=self.config["header"])

    @staticmethod
    def find_tweet_by_id(tweets, tweet_id):
        """
        Finds and returns a tweet from the list by user_id.
        """
        for tweet in tweets:
            if tweet["tweet_id"] == tweet_id:
                return tweet
        return None
