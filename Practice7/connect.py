import psycopg2
from config import load_config


def connect():
    """Connect to the PostgreSQL database"""

    connection = None

    try:
        params = load_config()

        connection = psycopg2.connect(**params)

        print("Connected to PostgreSQL successfully!")

        return connection

    except (Exception, psycopg2.DatabaseError) as error:
        print("Connection Error:", error)
        return None


if __name__ == "__main__":
    conn = connect()

    if conn:
        conn.close()
        print("Connection closed.")
