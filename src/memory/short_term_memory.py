import datetime

from src.database.postgres_database import PostgresDatabase


class ShortTermMemory:
    def __init__(self):
        postgres_db = PostgresDatabase("localhost", 5432, "postgres", "postgres", "root")
        self.db = postgres_db.get_connection()

    def save_into_memory(self, session_id, user_input, output):
        try:
            cursor = self.db.cursor()
            cursor.execute(
                "INSERT INTO short_term_memory (session_id, user_input, output,created_at) VALUES (%s, %s, %s, %s)",
                (session_id, user_input, output, datetime.datetime.now())
            )
            self.db.commit()
            cursor.close()
        except Exception as e:
            print("Failed to save into short term memory:", e)

    def get_short_term_memory(self, session_id):
        try:
            cursor = self.db.cursor()
            cursor.execute(
                "SELECT user_input, output FROM short_term_memory WHERE session_id = %s ORDER BY created_at DESC",
                (session_id,)
            )
            rows = cursor.fetchall()
            messages = []
            for row in rows:
                user_input, output = row
                messages.append({"role": "user", "content": user_input})
                messages.append({"role": "assistant", "content": output})
            cursor.close()
            return messages
        except Exception as e:
            print("Failed to get short term memory:", e)
            return None

    def clear_short_term_memory(self, session_id: str):
        try:
            cursor = self.db.cursor()
            cursor.execute("DELETE FROM short_term_memory WHERE session_id = %s", (session_id,))
            self.db.commit()
            cursor.close()
        except Exception as e:
            print("Failed to clear short term memory:", e)
