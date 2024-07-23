class TweetDetails:

    def __init__(self, tweet_id):
        self._tweet_id = tweet_id

    @property
    def tweet_id(self):
        return self._tweet_id

    @tweet_id.setter
    def tweet_id(self, value):
        self._tweet_id = value

    def to_dict(self):
        """
        Converts the UserDetails instance to a dictionary.
        """
        return {
            "tweet_id": self._tweet_id,
        }

    def __str__(self):
        return f"tweet_id={self.tweet_id}"
