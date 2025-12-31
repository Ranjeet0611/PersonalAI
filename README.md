PersonalAI is a privacy-focused, local AI assistant that combines the power of Ollama with a "Smart Memory" system. Unlike standard chatbots that forget everything once the session ends, PersonalAI uses a vector database to recall past context and provide more personalized responses over time.

✨ Key Features

    100% Local Inference: Powered by Ollama, ensuring your data never leaves your machine.

    Smart History Storage: Instead of just dumping text, it stores conversation embeddings in PostgreSQL (pgvector) for semantic retrieval.

    Agentic Memory: Uses LangChain to decide when to pull from long-term memory vs. short-term context.

    Modern Chat UI: A clean, responsive interface built with Gradio.


🚀 Getting Started
1. Prerequisites

    Ollama: Download and install Ollama.

    PostgreSQL: Ensure you have Postgres installed with the pgvector extension.

        Quick fix for the extension error: sudo apt install postgresql-17-pgvector (for Linux).

    Models: Pull your preferred model:
   ollama pull llama3

Since your project specifically uses Ollama for local inference and features "smart" history storage (utilizing the pgvector setup we discussed), the README should highlight those privacy and memory features.

Here is a tailored README.md for your PersonalAI project.
PersonalAI 🧠

PersonalAI is a privacy-focused, local AI assistant that combines the power of Ollama with a "Smart Memory" system. Unlike standard chatbots that forget everything once the session ends, PersonalAI uses a vector database to recall past context and provide more personalized responses over time.
✨ Key Features

    100% Local Inference: Powered by Ollama, ensuring your data never leaves your machine.

    Smart History Storage: Instead of just dumping text, it stores conversation embeddings in PostgreSQL (pgvector) for semantic retrieval.

    Agentic Memory: Uses LangGraph to decide when to pull from long-term memory vs. short-term context.

    Modern Chat UI: A clean, responsive interface built with Streamlit.

    Observability: Integrated with LangSmith to track agent logic and memory retrieval.

🛠️ Technical Stack

    LLM Engine: Ollama (Default: llama3 or mistral)

    Orchestration: LangGraph & LangChain

    Database: PostgreSQL with pgvector

    Frontend: Streamlit

    Language: Python 3.10+

🚀 Getting Started
1. Prerequisites

    Ollama: Download and install Ollama.

    PostgreSQL: Ensure you have Postgres installed with the pgvector extension.

        Quick fix for the extension error: sudo apt install postgresql-17-pgvector (for Linux).

    Models: Pull your preferred model:
    Bash

    ollama pull llama3

2. Installation

    Clone the Repo:

git clone https://github.com/Ranjeet0611/PersonalAI.git
cd PersonalAI

Install Dependencies:

pip install -r requirements.txt   

3 . Create Tables

    Long term memory
        
    CREATE TABLE IF NOT EXISTS public.long_term_memory
    (
        id integer NOT NULL DEFAULT nextval('long_term_memory_id_seq'::regclass),
        content text COLLATE pg_catalog."default",
        embedding vector(768),
        created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
        user_input text COLLATE pg_catalog."default",
        output text COLLATE pg_catalog."default",
        CONSTRAINT long_term_memory_pkey PRIMARY KEY (id)
    )
    
    TABLESPACE pg_default;
    
    ALTER TABLE IF EXISTS public.long_term_memory
        OWNER to postgres;

    Short term memory
    CREATE TABLE IF NOT EXISTS public.short_term_memory
    (
        id integer NOT NULL DEFAULT nextval('short_term_memory_id_seq'::regclass),
        user_input text COLLATE pg_catalog."default",
        output text COLLATE pg_catalog."default",
        created_at timestamp without time zone,
        session_id text COLLATE pg_catalog."default",
        CONSTRAINT short_term_memory_pkey PRIMARY KEY (id)
    )
    
    TABLESPACE pg_default;
    
    ALTER TABLE IF EXISTS public.short_term_memory
        OWNER to postgres;
        
