class UserDetails:

    def __init__(self, username, user_id):
        self._username = username
        self._user_id = user_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    def to_dict(self):
        """
        Converts the UserDetails instance to a dictionary.
        """
        return {
            "username": self.username,
            "user_id": self.user_id
        }
