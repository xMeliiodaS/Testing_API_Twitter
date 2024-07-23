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
        filtered_tweets = list(filter(lambda tweet: tweet["tweet_id"] == tweet_id, tweets))
        return filtered_tweets[0]

    @staticmethod
    def find_follower_by_user_id(followers, user_id):
        """
        Helper function to find a follower by user_id.

        Args:
            followers (list): The list of followers to search through.
            user_id (str): The user_id of the follower to find.

        Returns:
            dict: The follower with the matching user_id, or None if not found.
        """
        filtered_followers = list(filter(lambda follower: follower["user_id"] == user_id, followers))
        return filtered_followers[0]

    @staticmethod
    def find_user_media_by_user_id(media_list, user_id):
        """
        Finds and returns a user media item from the list by user_id.

        Args:
            media_list (list): The list of media items to search through.
            user_id (str): The user_id of the media item to find.

        Returns:
            dict: The media item with the matching user_id, or None if not found.
        """
        filtered_media = list(filter(lambda media: media["user"]["user_id"] == user_id, media_list))
        return filtered_media[0]
