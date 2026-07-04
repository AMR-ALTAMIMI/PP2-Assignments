import psycopg2
from config import load_config

def get_connection():
    config = load_config()
    return psycopg2.connect(**config)

if __name__ == "__main__":
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(f"Connected successfully to: {db_version[0]}")

        cur.close()
        conn.close()
    except Exception as error:
        print("Connection error:", error)
