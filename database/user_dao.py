class UserDAO:
    """
    A Class to the User Details Data Access Object
    """
    def __init__(self, db):
        self.db = db

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
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
        row = cursor.fetchone()

        # Convert the tuple to a dictionary
        if row:
            columns = [column[0] for column in cursor.description]
            return dict(zip(columns, row))
        return None

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

    def print_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            print(f"User ID: {user['user_id']}")
            print(f"Username: {user['username']}")
            print(f"Name: {user['name']}")
            print(f"Follower Count: {user['follower_count']}")
            print(f"Following Count: {user['following_count']}")
        else:
            print("User not found")

    def print_all_users(self):
        query = "SELECT * FROM users"
        cursor = self.db.execute_query(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)