"""Small test script to see if Python can connect to PostgreSQL"""
import os
import psycopg as ps
from dotenv import load_dotenv

load_dotenv()

# Constants
POSTGRES_HOST: str = os.environ["POSTGRES_HOST"]
POSTGRES_DB: str = os.environ["POSTGRES_DB"]
POSTGRES_USER: str = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD: str = os.environ["POSTGRES_PASSWORD"]
POSTGRES_PORT: str = os.environ["POSTGRES_PORT"]

def main() -> None:
    with ps.connect(
        host=POSTGRES_HOST,
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=POSTGRES_PORT,
    ) as db:
        with db.cursor() as cur:
            cur.execute("SELECT version();")
            version = cur.fetchone()
            print(f"--- Response from PostgreSQL ---\nVersion: {version}")


if __name__ == "__main__":
    main()