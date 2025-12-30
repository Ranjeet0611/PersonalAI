import psycopg2


class PostgresDatabase:
    def __init__(self, host, port, database, user, password):
        try:
            connection = psycopg2.connect(
                host=host,
                port=port,
                database=database,
                user=user,
                password=password
            )
            self.connection = connection
        except Exception as e:
            print(f"Error connecting to PostgreSQL database: {e}")
            self.connection = None

    def get_connection(self):
        return self.connection
