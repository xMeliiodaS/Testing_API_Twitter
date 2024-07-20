from infra.browser.configure_provider import ConfigProvider


class APIUserMedia:
    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_media(self):
        url = f'{self.config["url"]}/user/medias?user_id={self.config["user_id"]}&limit=10'
        return self._request.get_request(url, headers=self.config["header"])

    def post_user_media(self, user_media_body):
        return self._request.post_request(f'{self.config["url"]}/user/medias',
                                          self.config["header"], user_media_body)
