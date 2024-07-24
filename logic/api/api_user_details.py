from database.database import Database
from database.user_dao import UserDAO
from infra.browser.configure_provider import ConfigProvider
from logic.api.utils.db_utils import DBUtils


class APIUserDetails:
    ENDPOINT = '/user/details'
    USERNAME_PARAM = '?username='
    USER_ID_PARAM = '&user_id='

    def __init__(self, request):
        self._request = request
        self.config = ConfigProvider.load_config_json()
        self.db_path = self.config['db_path']

    def get_user_details(self, username, user_id):
        """
        Retrieve user details using the configured URL and headers.
        username (str): The username of the user.
        user_id (str): The ID of the user.
        Returns: The response from the API containing user details.
        """
        url = (f"{self.config['url']}{self.ENDPOINT}"
               f"{self.USERNAME_PARAM}{username}{self.USER_ID_PARAM}{user_id}")
        response = self._request.get_request(url, headers=self.config["header"])

        if response.ok:
            user_details = response.data
            db = DBUtils.initialize_database(self.db_path)
            DBUtils.add_user_to_db(db, user_details)
            user_dao = UserDAO(db)
            user_dao.print_user(user_id)
            db.close_connection()

        return response

    def post_user_details(self, user_name_details):
        """
        Send a POST request to update user details.
        user_name_details (dict): The user details to update.
        Returns: The response from the API.
        """
        return self._request.post_request(f'{self.config["url"]}{self.ENDPOINT}'
                                          , self.config["header"],
                                          user_name_details)
