from infra.api.api_wrapper import APIWrapper


class UserTweets:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_user_details(self, config, headers):
        """Requests to shuffle the deck with a specified number of decks.

        Args:
            config (dict): Contain all the params.
            headers (dict): The headers to include in the request.

        Returns:
            Response: The response from the API.
        """

        url = (f"{config['url']}/{config['end_url_tweets']}"
               f"?username={config['username']}"
               f"&user_id={config['user_id']}")
        return self._request.get_request(url, headers=headers)
