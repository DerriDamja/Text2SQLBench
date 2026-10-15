"""
(Eventually) Runs the Text2SQL Benchmark
"""

import os
import ollama
import psycopg as ps
from dotenv import load_dotenv

load_dotenv()

# Constants
POSTGRES_HOST: str = os.environ["POSTGRES_HOST"]
POSTGRES_DB: str = os.environ["POSTGRES_DB"]
POSTGRES_USER: str = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD: str = os.environ["POSTGRES_PASSWORD"]
POSTGRES_PORT: str = os.environ["POSTGRES_PORT"]
OLLAMA_HOST: str = os.environ["OLLAMA_HOST"]
OLLAMA_MODEL: str = os.environ["OLLAMA_MODEL"]

# PostgreSQL config
db = ps.connect(
    host=POSTGRES_HOST,
    dbname=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    port=POSTGRES_PORT,
)