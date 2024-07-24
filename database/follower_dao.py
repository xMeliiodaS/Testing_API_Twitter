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

    def add_follower(self, user_id, follower_user_id, follower_count, following_count, name):
        query = """
        INSERT INTO Follower (user_id, follower_user_id, follower_count, following_count, name)
        VALUES (?, ?, ?, ?, ?);
        """
        self.db.execute_query(query, (user_id, follower_user_id, follower_count, following_count, name))

    def get_followers(self, user_id):
        query = "SELECT follower_user_id, follower_count, following_count, name FROM Follower WHERE user_id = ?;"
        cursor = self.db.execute_query(query, (user_id,))
        return cursor.fetchall()

    def update_follower(self, user_id, follower_user_id, follower_count, following_count, name):
        query = """
        UPDATE Follower
        SET follower_count = ?, following_count = ?, name = ?
        WHERE user_id = ? AND follower_user_id = ?;
        """
        self.db.execute_query(query, (follower_count, following_count, name, user_id, follower_user_id))

    def delete_follower(self, user_id, follower_user_id):
        query = "DELETE FROM Follower WHERE user_id = ? AND follower_user_id = ?;"
        self.db.execute_query(query, (user_id, follower_user_id))
