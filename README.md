PersonalAI is a privacy-focused, local AI assistant that combines the power of Ollama with a "Smart Memory" system. Unlike standard chatbots that forget everything once the session ends, PersonalAI uses a vector database to recall past context and provide more personalized responses over time.

✨ Key Features

    100% Local Inference: Powered by Ollama, ensuring your data never leaves your machine.

    Smart History Storage: Instead of just dumping text, it stores conversation embeddings in PostgreSQL (pgvector) for semantic retrieval.

    Agentic Memory: Uses LangChain to decide when to pull from long-term memory vs. short-term context.

    Modern Chat UI: A clean, responsive interface built with Gradio.
