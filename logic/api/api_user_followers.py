from infra.browser.configure_provider import ConfigProvider


class APIUserFollowers:
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
        url = (f"{self.config['url']}/{self.config['user_followers_endpoint']}"
               f"?user_id={user_id}&limit={limit}")
        return self._request.get_request(url, headers=self.config["header"])

    def post_user_followers(self, follower_details):
        """
        Send a POST request to update follower details.
        follower_details (dict): The details of the followers to update.
        Returns: The response from the API.
        """
        return self._request.post_request(f'{self.config["url"]}/{self.config["user_followers_endpoint"]}',
                                          self.config["header"], follower_details)
