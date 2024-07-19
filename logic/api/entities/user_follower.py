class UserFollower:

    def __init__(self, user_id, limit):
        self._user_id = user_id
        self._limit = limit

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value

    def to_dict(self):
        """
        Converts the UserFollower instance to a dictionary.
        """
        return {
            "user_id": self.user_id,
            "limit": self.limit
        }
