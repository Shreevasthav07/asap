from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

database_url = (
    f"postgresql+psycopg2://"
    f"{user}:{password}@"
    f"{host}:{port}/{database}"
)

engine = create_engine(database_url)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        print("Database connection successful!")
        print("Test result:", result.scalar())

except Exception as e:
    print("Database connection failed.")
    print(e)