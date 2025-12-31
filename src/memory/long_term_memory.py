from src.database.postgres_database import PostgresDatabase
from langchain_classic.embeddings import OllamaEmbeddings
from src.constant import constant


class LongTermMemory:

    def __init__(self):
        self.memory_type = "long-term"
        postgres_db = PostgresDatabase("localhost", 5432, "postgres", "postgres", "root")
        self.db = postgres_db.get_connection()
        self.embeddings = OllamaEmbeddings(
            model=constant.EMBEDDING_MODEL_NAME
        )

    def save_into_memory(self, user_input, output):
        try:
            text_to_store = f"User: {user_input}\nAssistant: {output}"
            cursor = self.db.cursor()
            embedding = self.embeddings.embed_query(text_to_store)
            cursor.execute("INSERT INTO long_term_memory (user_input,content, embedding,output) VALUES (%s, %s,%s, %s)",
                           (user_input, text_to_store, embedding, output))
            self.db.commit()
            cursor.close()
        except Exception as e:
            print("Failed to save into long term memory:", e)

    def search_long_term(self, query: str, limit=3):
        query_embedding = self.embeddings.embed_query(query)
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT user_input,output
            FROM long_term_memory
            ORDER BY embedding <-> %s::vector
            LIMIT %s
            """,
            (query_embedding, limit)
        )
        messages = []
        for row in cursor.fetchall():
            user_input, output = row
            messages.append({"role": "user", "content": user_input})
            messages.append({"role": "assistant", "content": output})
        return messages
