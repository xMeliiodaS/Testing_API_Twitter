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
        row = cursor.fetchone()

        # Convert the tuple to a dictionary
        if row:
            columns = [column[0] for column in cursor.description]
            return dict(zip(columns, row))
        return None

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

    def print_tweet(self, tweet_id):
        tweet = self.get_tweets(tweet_id)
        if tweet:
            print(f"Tweet ID: {tweet['tweet_id']}")
            print(f"User ID: {tweet['user_id']}")
            print(f"Text: {tweet['text']}")
        else:
            print("Tweet not found")

    def print_all_tweets(self):
        query = "SELECT * FROM Tweets_details"
        cursor = self.db.execute_query(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)