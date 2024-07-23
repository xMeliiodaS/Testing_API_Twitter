class Utils:

    @staticmethod
    def find_tweet_by_id(tweets, tweet_id):
        """
        Finds a tweet by its ID in a list of tweets.

        Args:
            tweets (list): The list of tweets to search through.
            tweet_id (str): The ID of the tweet to find.

        Returns:
            dict: The tweet with the matching ID, or None if not found.
        """
        for tweet in tweets:
            if tweet["tweet_id"] == tweet_id:
                return tweet
        return None

    @staticmethod
    def find_follower_by_user_id(followers, user_id):
        """
        Helper function to find a follower by user_id.
        """
        for follower in followers:
            if follower["user_id"] == user_id:
                return follower
        return None

    @staticmethod
    def find_user_media_by_user_id(media_list, user_id):
        """
        Finds and returns a user media item from the list by user_id.
        """
        for media in media_list:
            if media["user"]["user_id"] == user_id:
                return media
        return None
