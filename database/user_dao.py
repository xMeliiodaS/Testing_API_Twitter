class UserDAO:
    """
    A Class to the User Details Data Access Object
    """
    def __init__(self, db):
        self.db = db

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Users_details (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            name TEXT NOT NULL,
            follower_count INTEGER,
            following_count INTEGER
        );
        """
        self.db.execute_query(query)

    def add_user(self, user):
        query = '''
        INSERT INTO users (user_id, username, name, follower_count, following_count)
        VALUES (?, ?, ?, ?, ?);
        '''

        params = (user['user_id'], user['username'], user['name'],
                  user['follower_count'], user['following_count'])
        self.db.execute_query(query, params)

    def get_user(self, user_id):
        query = '''
        SELECT * FROM users WHERE user_id = ?
        '''
        cursor = self.db.execute_query(query, (user_id,))

        # Fetch one row
        return cursor.fetchone()

    def update_user(self, user):
        query = '''
        UPDATE users
        SET username = ?, name = ?, follower_count = ?, following_count = ?
        WHERE user_id = ?
        '''

        params = (user['username'], user['follower_count'], user['following_count'],
                  user['description'], user['user_id'])
        self.db.execute_query(query, params)

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE user_id = ?;"
        self.db.execute_query(query, (user_id,))
