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

    def add_tweet(self, tweet):
        query = """
        INSERT INTO Tweets_details (tweet_id, user_id, text)
        VALUES (?, ?, ?);
        """
        params = (tweet['tweet_id'], tweet['user_id'], tweet['text'])
        self.db.execute_query(query, params)

    def get_tweets(self, tweet_id):
        query = "SELECT * FROM Tweets_details WHERE tweet_id = ?;"
        cursor = self.db.execute_query(query, (tweet_id,))
        return cursor.fetchone()

    def update_tweet(self, tweet):
        query = """
        UPDATE Tweets_details
        SET text = ?
        WHERE tweet_id = ?;
        """
        params = (tweet['text'], tweet['tweet_id'])
        self.db.execute_query(query, params)

    def delete_tweet(self, tweet_id):
        query = "DELETE FROM Tweets_details WHERE tweet_id = ?;"
        self.db.execute_query(query, (tweet_id,))
