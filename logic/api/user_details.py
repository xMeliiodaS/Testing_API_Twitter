from infra.api.api_wrapper import APIWrapper


class UserDetails:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_user_details(self, url, headers, username, user_id):
        """Requests to shuffle the deck with a specified number of decks.

        Args:
            url (str): The base URL of the API.
            headers (dict): The headers to include in the request.

        Returns:
            Response: The response from the API.
        """
        url = f"{url}/user/details?username={username}&user_id={user_id}"
        return self._request.get_request(url, headers=headers)
