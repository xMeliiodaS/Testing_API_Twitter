from infra.browser.configure_provider import ConfigProvider


class APIUserFollowers:
    ENDPOINT = '/user/followers'
    USER_ID = '?user_id='
    LIMIT = '&limit='

    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_followers(self, user_id, limit):
        """
        Retrieve user followers using the configured URL with parameters and headers.
        user_id (str): The ID of the user.
        limit (int): The maximum number of followers to retrieve.
        Returns: The response from the API containing user followers.
        """
        url = (f"{self.config['url']}{self.ENDPOINT}"
               f"{self.USER_ID}{user_id}{self.LIMIT}{limit}")
        return self._request.get_request(url, headers=self.config["header"])

    def post_user_followers(self, follower_details):
        """
        Send a POST request to update follower details.
        follower_details (dict): The details of the followers to update.
        Returns: The response from the API.
        """
        return self._request.post_request(f'{self.config["url"]}{self.ENDPOINT}',
                                          self.config["header"], follower_details)
