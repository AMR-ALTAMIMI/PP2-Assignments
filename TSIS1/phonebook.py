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

    sql = """
    SELECT
        c.name,
        c.email,
        c.birthday,
        g.name,
        p.phone,
        p.type
    FROM contacts c
    LEFT JOIN groups g
        ON c.group_id = g.id
    LEFT JOIN phones p
        ON c.id = p.contact_id
    ORDER BY c.id;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute(sql)

                rows = cur.fetchall()

                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No contacts found.")

    except Exception as error:
        print(error)

def search_contacts_fn(search_text):

    sql = "SELECT * FROM search_contacts(%s);"

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute(sql,(search_text,))

                rows = cur.fetchall()

                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No contacts found.")

    except Exception as error:
        print(error)
     def insert_or_update():

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group: ")
    phone = input("Phone: ")
    phone_type = input("Type (home/work/mobile): ")

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute(
                    "CALL insert_or_update_user(%s,%s,%s,%s,%s,%s)",
                    (
                        name,
                        email,
                        birthday,
                        group,
                        phone,
                        phone_type
                    )
                )

        print("Contact saved successfully.")

    except Exception as error:
        print(error)

def insert_from_csv(filename="contacts.csv"):

    try:

        config = load_config()

        with open(filename, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:

                    for row in reader:

                        cur.execute(
                            "CALL insert_or_update_user(%s,%s,%s,%s,%s,%s)",
                            (
                                row["name"],
                                row["email"],
                                row["birthday"],
                                row["group"],
                                row["phone"],
                                row["type"]
                            )
                        )

        print("CSV imported successfully.")

    except Exception as error:
        print(error) 
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
import json


# Search by email
def search_by_email(email):
    sql = """
    SELECT name, email, birthday
    FROM contacts
    WHERE email ILIKE %s;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, ("%" + email + "%",))
                rows = cur.fetchall()

                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No contacts found.")

    except Exception as error:
        print(error)


# Filter contacts by group
def filter_by_group(group):
    sql = """
    SELECT c.name,
           c.email,
           c.birthday,
           g.name
    FROM contacts c
    JOIN groups g
    ON c.group_id = g.id
    WHERE g.name=%s;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (group,))
                rows = cur.fetchall()

                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No contacts in this group.")

    except Exception as error:
        print(error)


# Sort contacts
def sort_contacts(order):

    sql = f"""
    SELECT name,email,birthday
    FROM contacts
    ORDER BY {order};
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)

                rows = cur.fetchall()

                for row in rows:
                    print(row)

    except Exception as error:
        print(error)


# Add phone
def add_phone(name, phone, phone_type):

    sql = "CALL add_phone(%s,%s,%s);"

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone, phone_type))

        print("Phone added successfully.")

    except Exception as error:
        print(error)


# Move contact to another group
def move_to_group(name, group):

    sql = "CALL move_to_group(%s,%s);"

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, group))

        print("Contact moved.")

    except Exception as error:
        print(error)
      # Export contacts to JSON
def export_json():

    import json

    sql = """
    SELECT
        c.name,
        c.email,
        c.birthday,
        g.name,
        p.phone,
        p.type
    FROM contacts c
    LEFT JOIN groups g
        ON c.group_id = g.id
    LEFT JOIN phones p
        ON c.id = p.contact_id;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute(sql)
                rows = cur.fetchall()

                contacts = []

                for row in rows:

                    contacts.append({
                        "name": row[0],
                        "email": row[1],
                        "birthday": str(row[2]),
                        "group": row[3],
                        "phone": row[4],
                        "type": row[5]
                    })

                with open("contacts.json", "w", encoding="utf-8") as file:
                    json.dump(contacts, file, indent=4)

        print("Contacts exported successfully!")

    except Exception as error:
        print(error)


# Import contacts from JSON
def import_json():

    import json

    try:

        with open("contacts.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)

        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                for contact in contacts:

                    cur.execute(
                        "SELECT id FROM contacts WHERE name=%s",
                        (contact["name"],)
                    )

                    exist = cur.fetchone()

                    if exist:

                        answer = input(
                            f"{contact['name']} already exists. Skip(s) / Overwrite(o): "
                        )

                        if answer.lower() == "s":
                            continue

                        cur.execute("""
                        UPDATE contacts
                        SET email=%s,
                            birthday=%s
                        WHERE name=%s
                        """,
                        (
                            contact["email"],
                            contact["birthday"],
                            contact["name"]
                        ))

                    else:

                        cur.execute("""
                        INSERT INTO contacts(name,email,birthday)
                        VALUES(%s,%s,%s)
                        """,
                        (
                            contact["name"],
                            contact["email"],
                            contact["birthday"]
                        ))

        print("JSON imported successfully!")

    except Exception as error:
        print(error)
  

def main_menu():

   

    while True:

        print("\n================ PHONEBOOK ================")
        print("1. Show all contacts")
        print("2. Insert / Update contact")
        print("3. Import CSV")
        print("4. Search contact")
        print("5. Pagination")
        print("6. Delete contact")
        print("7. Filter by group")
        print("8. Search by email")
        print("9. Sort contacts")
        print("10. Add phone")
        print("11. Move contact to group")
        print("12. Export JSON")
        print("13. Import JSON")
        print("0. Exit")
        print("===========================================")

        choice = input("Choose: ")

        if choice == "1":
            show_all_contacts()

        elif choice == "2":
            username = input("Name: ")
            phone = input("Phone: ")
            insert_or_update(username, phone)

        elif choice == "3":
            filename = input("CSV file (default contacts.csv): ") or "contacts.csv"
            insert_from_csv(filename)

        elif choice == "4":
            text = input("Search: ")
            search_contacts_fn(text)

        elif choice == "5":

            limit = 3
            offset = 0

            while True:

                get_contacts_paginated_fn(limit, offset)

                cmd = input("next / prev / quit : ").lower()

                if cmd == "next":
                    offset += limit

                elif cmd == "prev":
                    offset = max(0, offset - limit)

                else:
                    break

        elif choice == "6":
            identifier = input("Username or Phone: ")
            delete_contact_proc(identifier)

        elif choice == "7":
            group = input("Group: ")
            filter_by_group(group)

        elif choice == "8":
            email = input("Email: ")
            search_by_email(email)

        elif choice == "9":

            print("1. Name")
            print("2. Birthday")
            print("3. Date Added")

            s = input("Choose: ")

            if s == "1":
                sort_contacts("name")
            elif s == "2":
                sort_contacts("birthday")
            else:
                sort_contacts("created_at")

        elif choice == "10":

            name = input("Name: ")
            phone = input("Phone: ")
            phone_type = input("Type (home/work/mobile): ")

            add_phone(name, phone, phone_type)

        elif choice == "11":

            name = input("Name: ")
            group = input("Group: ")

            move_to_group(name, group)

        elif choice == "12":
            export_json()

        elif choice == "13":
            import_json()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main_menu()               
