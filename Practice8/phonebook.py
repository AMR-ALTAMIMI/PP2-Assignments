import psycopg2
from config import load_config
import csv

def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL UNIQUE,
        phone VARCHAR(20) NOT NULL
    );
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
        print("PhoneBook table verified/created successfully!")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while creating table:", error)

def show_all_contacts():
    sql = "SELECT id, username, phone FROM phonebook ORDER BY id;"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
                else:
                    print("Phonebook is empty.")
    except Exception as error:
        print("Error showing contacts:", error)

# [Req 1] Call Search Function
def search_contacts_fn(search_text):
    sql = "SELECT * FROM search_contacts(%s);"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (search_text,))
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(f"Found -> ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
                else:
                    print("No records matching the pattern found.")
    except Exception as error:
        print("Error execution search function:", error)

# [Req 2] Call Upsert Procedure
def insert_or_update(username, phone):
    sql = "CALL insert_or_update_user(%s, %s);"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username, phone))
        print(f"Contact data processed for user '{username}'.")
    except Exception as error:
        print("Procedure execution error:", error)

# [Req 3] Call Bulk Input Loop and Validation Procedure
def insert_from_csv(filename="contacts.csv"):
    usernames = []
    phones = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Aligns safely with standard CSV header fields: 'name' and 'phone'
                usernames.append(row["name"])
                phones.append(row["phone"])
        
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execution with OUT parameters variables initialized explicitly 
                cur.execute("CALL insert_many_contacts(%s, %s, CAST(NULL AS VARCHAR[]), CAST(NULL AS VARCHAR[]));", (usernames, phones))
                result = cur.fetchone()
                
                print("Bulk insertion execution finished.")
                if result and (result[0] or result[1]):
                    print("\n⚠️ The following rows failed internal database constraints/validation:")
                    for u, p in zip(result[0], result[1]):
                        print(f" -> Rejected Name: {u} | Phone Number: {p}")
                else:
                    print("All records verified and synchronized perfectly.")
    except FileNotFoundError:
        print(f"CSV operation aborted: '{filename}' not found.")
    except Exception as error:
        print("Error executing bulk management procedure:", error)

# [Req 4] Call Pagination Function
def get_contacts_paginated_fn(limit, offset):
    sql = "SELECT * FROM get_contacts_paginated(%s, %s);"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (limit, offset))
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
                else:
                    print("No data available within this page scope.")
    except Exception as error:
        print("Pagination query error:", error)

# [Req 5] Call Consolidated Deletion Procedure
def delete_contact_proc(identifier):
    sql = "CALL delete_contact(%s);"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (identifier,))
        print(f"Deletion logic applied for identifier target: '{identifier}'.")
    except Exception as error:
        print("Error executing delete procedure:", error)


def main_menu():
    create_table()
    while True:
        print("\n================ PHONEBOOK MENU ================")
        print("1. Show all records")
        print("2. Insert/Update Single User (Procedure)")
        print("3. Import and Validate Bulk CSV Data (Procedure)")
        print("4. Search Pattern Match (Function)")
        print("5. View contacts with pagination (Function)")
        print("6. Delete contact by Username or Phone (Procedure)")
        print("0. Exit Application")
        print("=================================================")
        
        choice = input("Select an option: ").strip()

        if choice == "1":
            show_all_contacts()
        elif choice == "2":
            username = input("Enter Name: ")
            phone = input("Enter Phone: ")
            insert_or_update(username, phone)
        elif choice == "3":
            filename = input("Enter CSV file path (Default: contacts.csv): ") or "contacts.csv"
            insert_from_csv(filename)
        elif choice == "4":
            text = input("Enter Search Text (Matches Name/Phone pattern): ")
            search_contacts_fn(text)
        elif choice == "5":
            try:
                limit = int(input("Page Size Limit: "))
                offset = int(input("Offset Index starting point: "))
                get_contacts_paginated_fn(limit, offset)
            except ValueError:
                print("Invalid input numbers.")
        elif choice == "6":
            identifier = input("Enter the Username or Phone number to delete: ")
            delete_contact_proc(identifier)
        elif choice == "0":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid configuration chosen. Try again.")

if __name__ == "__main__":
    main_menu()               
