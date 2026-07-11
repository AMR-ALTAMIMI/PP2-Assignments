import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="postgres",
        user="postgres",
        password="Amr12345",
        port="5432"
    )

    print("Connected!")

    cur = conn.cursor()
    cur.execute("SELECT datname FROM pg_database;")

    for db in cur.fetchall():
        print(db[0])

    cur.close()
    conn.close()

except Exception as e:
    print(e)
