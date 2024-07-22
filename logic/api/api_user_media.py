from infra.browser.configure_provider import ConfigProvider


class APIUserMedia:
    ENDPOINT = '/user/medias'
    USER_ID_PARAM = '?user_id='
    LIMIT = '&limit='

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
        url = f'{self.config["url"]}{self.ENDPOINT}{self.USER_ID_PARAM}{user_id}{self.LIMIT}{limit}'
        return self._request.get_request(url, headers=self.config["header"])

    def post_user_media(self, user_media_body):
        """
        Send a POST request to update user media.
        user_media_body (dict): The media details to update.
        Returns: The response from the API.
        """
        return self._request.post_request(f'{self.config["url"]}{self.ENDPOINT}',
                                          self.config["header"], user_media_body)

    @staticmethod
    def find_user_media_by_user_id(media_list, user_id):
        """
        Finds and returns a user media item from the list by user_id.
        """
        for media in media_list:
            if media["user"]["user_id"] == user_id:
                return media
        return None
