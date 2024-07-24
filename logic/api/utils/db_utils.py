from database.database import Database
from database.follower_dao import FollowerDAO
from database.tweet_dao import TweetDAO
from database.user_dao import UserDAO


class DBUtils:
    @staticmethod
    def initialize_database(db_file):
        db = Database(db_file)
        db.create_connection()

        # Initialize DAOs
        user_dao = UserDAO(db)
        tweet_dao = TweetDAO(db)
        follower_dao = FollowerDAO(db)

        # Create tables if they don't exist
        user_dao.create_table()
        tweet_dao.create_table()
        follower_dao.create_table()

        return db

    @staticmethod
    def add_user_to_db(db, user_details):
        user_dao = UserDAO(db)
        user_dao.add_user(user_details)

    @staticmethod
    def add_tweet_to_db(db, tweet):
        tweet_dao = TweetDAO(db)
        tweet_dao.add_tweet(tweet)

    @staticmethod
    def add_follower_to_db(db, follower):
        follower_dao = FollowerDAO(db)
        follower_dao.add_follower(follower)
