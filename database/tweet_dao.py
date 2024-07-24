# tweet_dao.py
class TweetDAO:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Tweets_details (
            tweet_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            text TEXT
        );
        """
        self.db.execute_query(query)

    def add_tweet(self, tweet_id, user_id, text):
        query = """
        INSERT INTO Tweets_details (tweet_id, user_id, text)
        VALUES (?, ?, ?, ?);
        """
        self.db.execute_query(query, (tweet_id, user_id, text))

    def get_tweets_by_user_id(self, user_id):
        query = "SELECT tweet_id, text, creation_date FROM Tweets_details WHERE user_id = ?;"
        cursor = self.db.execute_query(query, (user_id,))
        return cursor.fetchall()

    def update_tweet(self, tweet_id, text):
        query = """
        UPDATE Tweets_details
        SET text = ?
        WHERE tweet_id = ?;
        """
        self.db.execute_query(query, (text, tweet_id))

    def delete_tweet(self, tweet_id):
        query = "DELETE FROM Tweets_details WHERE tweet_id = ?;"
        self.db.execute_query(query, (tweet_id,))
