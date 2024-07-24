from database.database import Database
from database.user_dao import UserDAO
from database.follower_dao import FollowerDAO
from database.tweet_dao import TweetDAO
from infra.api.api_wrapper import APIWrapper
from logic.api.api_user_details import APIUserDetails
from infra.browser.configure_provider import ConfigProvider


def initialize_database(db_path):
    db = Database(db_path)
    db.create_connection()

    user_dao = UserDAO(db)
    tweet_dao = TweetDAO(db)
    follower_dao = FollowerDAO(db)

    user_dao.create_table()
    tweet_dao.create_table()
    follower_dao.create_table()

    return db


if __name__ == "__main__":
    # Load configuration
    config = ConfigProvider.load_config_json()
    db_path = config['db_path']

    # Initialize database
    db = initialize_database(db_path)

    # Proceed with your application logic, e.g., API operations
    api_request = APIWrapper()
    user_details = APIUserDetails(api_request)

    # Example of using APIUserDetails
    response = user_details.get_user_details(config["my_username"], config["my_user_id"])

    db.close_connection()
