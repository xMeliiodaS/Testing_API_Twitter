from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider


class APIUserTweets:
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
        url = (f"{self.config['url']}/{self.config['user_tweets_endpoint']}"
               f"?username={username}&limit={limit}&user_id={user_id}"
               f"&include_replies={include_replies}&include_pinned={include_pinned}")
        return self._request.get_request(url, headers=self.config["header"])
