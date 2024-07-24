# follower_dao.py
class FollowerDAO:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Follower (
            user_id INTEGER,
            follower_user_id INTEGER,
            follower_count INTEGER,
            following_count INTEGER,
            name TEXT,
            PRIMARY KEY (user_id, follower_user_id)
        );
        """
        self.db.execute_query(query)

    def add_follower(self, follower):
        query = """
        INSERT INTO Follower (user_id, follower_user_id, follower_count, following_count, name)
        VALUES (?, ?, ?, ?, ?);
        """
        params = (follower['user_id'], follower['follower_user_id'], follower['follower_count'],
                  follower['following_count'], follower['name'])
        self.db.execute_query(query, params)

    def get_followers(self, user_id, follower_user_id):
        query = "SELECT * FROM Follower WHERE user_id = ? AND follower_user_id = ?;"
        cursor = self.db.execute_query(query, (user_id, follower_user_id))
        return cursor.fetchone()

    def update_follower(self, follower):
        query = """
        UPDATE Follower
        SET follower_count = ?, following_count = ?, name = ?
        WHERE user_id = ? AND follower_user_id = ?;
        """
        params = (follower['follower_count'], follower['following_count'], follower['name'],
                  follower['user_id'], follower['follower_user_id'])
        self.db.execute_query(query, params)

    def delete_follower(self, user_id, follower_user_id):
        query = "DELETE FROM Follower WHERE user_id = ? AND follower_user_id = ?;"
        self.db.execute_query(query, (user_id, follower_user_id))
