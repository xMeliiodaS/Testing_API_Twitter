from infra.browser.configure_provider import ConfigProvider


class APIUserDetails:
    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_details(self, username, user_id):
        """
        Retrieve user details using the configured URL and headers.
        username (str): The username of the user.
        user_id (str): The ID of the user.
        Returns: The response from the API containing user details.
        """
        url = (f"{self.config['url']}/{self.config['user_details_endpoint']}"
               f"?username={username}&user_id={user_id}")
        return self._request.get_request(url, headers=self.config["header"])

    def post_user_details(self, user_name_details):
        """
        Send a POST request to update user details.
        user_name_details (dict): The user details to update.
        Returns: The response from the API.
        """
        return self._request.post_request(f'{self.config["url"]}/{self.config["user_details_endpoint"]}'
                                          , self.config["header"],
                                          user_name_details)
