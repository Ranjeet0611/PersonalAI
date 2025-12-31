PersonalAI is a privacy-focused, local AI assistant that combines the power of Ollama with a "Smart Memory" system. Unlike standard chatbots that forget everything once the session ends, PersonalAI uses a vector database to recall past context and provide more personalized responses over time.

✨ Key Features

    100% Local Inference: Powered by Ollama, ensuring your data never leaves your machine.

    Smart History Storage: Instead of just dumping text, it stores conversation embeddings in PostgreSQL (pgvector) for semantic retrieval.

    Agentic Memory: Uses LangChain to decide when to pull from long-term memory vs. short-term context.

    Modern Chat UI: A clean, responsive interface built with Gradio.

🛠️ Technical Stack

    LLM Engine: Ollama (Default: llama3 or mistral)

    Orchestration: LangChain

    Database: PostgreSQL with pgvector

    Frontend: Gradio

    Language: Python 3.10+

🚀 Getting Started
    1. Prerequisites

        Ollama: Download and install Ollama.
    
        PostgreSQL: Ensure you have Postgres installed with the pgvector extension.
    
            Quick fix for the extension error: sudo apt install postgresql-17-pgvector (for Linux).
    
        Models: Pull your preferred model:
    
            ollama run llama3.1:8b
            ollama pull nomic-embed-text:v1.5

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
        

 4. Run Application
    
         main.py - for CLI application
         agent.py - for web based application

<img width="1882" height="603" alt="image" src="https://github.com/user-attachments/assets/d6ced0f9-ef41-4224-afe3-002b18ac77ac" />


           
