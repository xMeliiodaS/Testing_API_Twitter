from infra.browser.configure_provider import ConfigProvider


class APIUserMedia:
    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_media(self, user_id, limit):
        """
        Retrieve user media using the configured URL with parameters and headers.
        user_id (str): The ID of the user.
        limit (int): The maximum number of media items to retrieve.
        Returns: The response from the API containing user media.
        """
        url = f'{self.config["url"]}/{self.config["user_medias_endpoint"]}' \
              f'?user_id={user_id}&limit={limit}'
        return self._request.get_request(url, headers=self.config["header"])

    def post_user_media(self, user_media_body):
        """
        Send a POST request to update user media.
        user_media_body (dict): The media details to update.
        Returns: The response from the API.
        """
        return self._request.post_request(f'{self.config["url"]}/{self.config["user_medias_endpoint"]}',
                                          self.config["header"], user_media_body)
