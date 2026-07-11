import csv
import json
from connect import create_connection

connection = create_connection()
cursor = connection.cursor()

def add_contact():
    connection = create_connection()
    cursor = connection.cursor()

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    birthday = input("Enter Birthday (YYYY-MM-DD): ")
    group = input("Enter Group (Family/Work/Friend/Other): ")
    phone = input("Enter Phone Number: ")
    phone_type = input("Phone Type (home/work/mobile): ")

    cursor.execute(
        "SELECT id FROM groups WHERE name=%s",
        (group,)
    )
    result = cursor.fetchone()

    if result:
        group_id = result[0]
    else:
        cursor.execute(
            "INSERT INTO groups(name) VALUES(%s) RETURNING id",
            (group,)
        )
        group_id = cursor.fetchone()[0]

    cursor.execute(
        """
        INSERT INTO contacts(name,email,birthday,group_id)
        VALUES(%s,%s,%s,%s)
        RETURNING id
        """,
        (name, email, birthday, group_id)
    )
    contact_id = cursor.fetchone()[0]

    cursor.execute(
        """
        INSERT INTO phones(contact_id,phone,type)
        VALUES(%s,%s,%s)
        """,
        (contact_id, phone, phone_type)
    )

    connection.commit()
    print("Contact added successfully!")
    cursor.close()
    connection.close()

def show_contacts():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
    SELECT
        c.id,
        c.name,
        c.email,
        c.birthday,
        g.name,
        p.phone,
        p.type
    FROM contacts c
    LEFT JOIN groups g
        ON c.group_id=g.id
    LEFT JOIN phones p
        ON c.id=p.contact_id
    ORDER BY c.id
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\n------ Contact List ------")
    for row in rows:
        print(f"ID       : {row[0]}")
        print(f"Name     : {row[1]}")
        print(f"Email    : {row[2]}")
        print(f"Birthday : {row[3]}")
        print(f"Group    : {row[4]}")
        print(f"Phone    : {row[5]}")
        print(f"Type     : {row[6]}")
        print("-" * 35)

    cursor.close()
    connection.close()

def search_contact():
    connection = create_connection()
    cursor = connection.cursor()

    keyword = input("Enter Name / Phone / Email: ")
    cursor.execute(
        "SELECT * FROM search_contacts(%s)",
        (keyword,)
    )
    rows = cursor.fetchall()

    if rows:
        print("\n------ Search Result ------")
        for row in rows:
            print(f"Name     : {row[0]}")
            print(f"Email    : {row[1]}")
            print(f"Birthday : {row[2]}")
            print(f"Group    : {row[3]}")
            print(f"Phone    : {row[4]}")
            print("-"*30)
    else:
        print("No contact found!")

    cursor.close()
    connection.close()

def search_email():
    connection = create_connection()
    cursor = connection.cursor()

    email = input("Enter email keyword: ")
    query = """
    SELECT name,email
    FROM contacts
    WHERE email ILIKE %s
    """
    cursor.execute(query, ('%' + email + '%',))
    rows = cursor.fetchall()

    if rows:
        print("\n------ Email Search ------")
        for row in rows:
            print(f"Name  : {row[0]}")
            print(f"Email : {row[1]}")
            print("-"*25)
    else:
        print("No contact found!")

    cursor.close()
    connection.close()

def filter_group():
    connection = create_connection()
    cursor = connection.cursor()

    group = input("Enter Group: ")
    query = """
    SELECT c.name,
           c.email,
           p.phone
    FROM contacts c
    JOIN groups g
      ON c.group_id=g.id
    LEFT JOIN phones p
      ON c.id=p.contact_id
    WHERE g.name=%s
    """
    cursor.execute(query, (group,))
    rows = cursor.fetchall()

    if rows:
        print("\n------ Group Contacts ------")
        for row in rows:
            print(f"Name  : {row[0]}")
            print(f"Email : {row[1]}")
            print(f"Phone : {row[2]}")
            print("-"*25)
    else:
        print("No contacts found!")

    cursor.close()
    connection.close()

def sort_contacts():
    connection = create_connection()
    cursor = connection.cursor()

    print("1. Name")
    print("2. Birthday")
    print("3. Date Added")
    choice = input("Sort By: ")

    if choice == "1":
        order = "name"
    elif choice == "2":
        order = "birthday"
    else:
        order = "id"

    query = f"""
    SELECT id,name,email,birthday
    FROM contacts
    ORDER BY {order}
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()

def update_contact():
    connection = create_connection()
    cursor = connection.cursor()

    name = input("Enter Contact Name: ")
    new_email = input("Enter New Email: ")
    new_birthday = input("Enter New Birthday (YYYY-MM-DD): ")
    new_group = input("Enter New Group: ")

    cursor.execute(
        "SELECT id FROM groups WHERE name=%s",
        (new_group,)
    )
    group = cursor.fetchone()

    if group:
        group_id = group[0]
    else:
        cursor.execute(
            "INSERT INTO groups(name) VALUES(%s) RETURNING id",
            (new_group,)
        )
        group_id = cursor.fetchone()[0]

    query = """
    UPDATE contacts
    SET email=%s,
        birthday=%s,
        group_id=%s
    WHERE name=%s
    """
    cursor.execute(
        query,
        (new_email, new_birthday, group_id, name)
    )
    connection.commit()

    if cursor.rowcount > 0:
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

    cursor.close()
    connection.close()

def delete_contact():
    connection = create_connection()
    cursor = connection.cursor()

    keyword = input("Enter Name or Phone: ")
    cursor.execute(
        "CALL delete_contact(%s)",
        (keyword,)
    )
    connection.commit()
    print("Delete operation completed!")
    cursor.close()
    connection.close()

def add_phone():
    connection = create_connection()
    cursor = connection.cursor()

    name = input("Enter Contact Name: ")
    phone = input("Enter Phone Number: ")
    phone_type = input("Enter Type (home/work/mobile): ")

    cursor.execute(
        "CALL add_phone(%s,%s,%s)",
        (name, phone, phone_type)
    )
    connection.commit()
    print("Phone added successfully!")
    cursor.close()
    connection.close()

def move_group():
    connection = create_connection()
    cursor = connection.cursor()

    name = input("Enter Contact Name: ")
    group = input("Enter New Group: ")

    cursor.execute(
        "CALL move_to_group(%s,%s)",
        (name, group)
    )
    connection.commit()
    print("Contact moved successfully!")
    cursor.close()
    connection.close()

def pagination():
    connection = create_connection()
    cursor = connection.cursor()

    limit = 5
    offset = 0

    while True:
        cursor.execute(
            "SELECT * FROM get_contacts(%s,%s)",
            (limit, offset)
        )
        rows = cursor.fetchall()
        print()
        for row in rows:
            print(row)

        print("\nN = Next")
        print("P = Previous")
        print("Q = Quit")
        choice = input("Choice: ").lower()

        if choice == "n":
            offset += limit
        elif choice == "p":
            offset = max(0, offset - limit)
        elif choice == "q":
            break

    cursor.close()
    connection.close()

def import_csv():
    connection = create_connection()
    cursor = connection.cursor()

    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "SELECT id FROM groups WHERE name=%s",
                (row["group"],)
            )
            result = cursor.fetchone()

            if result:
                group_id = result[0]
            else:
                cursor.execute(
                    "INSERT INTO groups(name) VALUES(%s) RETURNING id",
                    (row["group"],)
                )
                group_id = cursor.fetchone()[0]

            cursor.execute("""
            INSERT INTO contacts(name,email,birthday,group_id)
            VALUES(%s,%s,%s,%s)
            RETURNING id
            """,
            (row["name"], row["email"], row["birthday"], group_id))
            contact_id = cursor.fetchone()[0]

            cursor.execute("""
            INSERT INTO phones(contact_id,phone,type)
            VALUES(%s,%s,%s)
            """,
            (contact_id, row["phone"], row["type"]))

    connection.commit()
    print("CSV Imported Successfully!")
    cursor.close()
    connection.close()

def export_json():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        c.name,
        c.email,
        c.birthday,
        g.name,
        p.phone,
        p.type
    FROM contacts c
    LEFT JOIN groups g ON c.group_id=g.id
    LEFT JOIN phones p ON c.id=p.contact_id
    """)
    rows = cursor.fetchall()

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

    with open("contacts.json", "w") as file:
         json.dump(contacts, file, indent=4)

    print("JSON Exported Successfully!")
    cursor.close()
    connection.close()

def import_json():
    connection = create_connection()
    cursor = connection.cursor()

    with open("contacts.json", "r") as file:
        contacts = json.load(file)

    for contact in contacts:
        cursor.execute(
            "SELECT id FROM contacts WHERE name=%s",
            (contact["name"],)
        )
        exists = cursor.fetchone()

        if exists:
            choice = input(f"{contact['name']} exists. Skip(S) / Overwrite(O): ").lower()
            if choice == "s":
                continue
            cursor.execute(
                "DELETE FROM contacts WHERE id=%s",
                (exists[0],)
            )

        cursor.execute(
            "SELECT id FROM groups WHERE name=%s",
            (contact["group"],)
        )
        result = cursor.fetchone()

        if result:
            group_id = result[0]
        else:
            cursor.execute(
                """
                INSERT INTO groups(name)
                VALUES(%s)
                RETURNING id
                """,
                (contact["group"],)
            )
            group_id = cursor.fetchone()[0]

        cursor.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES(%s,%s,%s,%s)
        RETURNING id
        """,
        (contact["name"], contact["email"], contact["birthday"], group_id))
        contact_id = cursor.fetchone()[0]

        cursor.execute("""
        INSERT INTO phones(contact_id, phone, type)
        VALUES(%s,%s,%s)
        """,
        (contact_id, contact["phone"], contact["type"]))

    connection.commit()
    print("JSON Imported Successfully!")
    cursor.close()
    connection.close()


# Main Menu Loop
while True:
    print("\n========== PHONEBOOK ==========")
    print("1. Add Contact")
    print("2. Import CSV")
    print("3. Show Contacts")
    print("4. Search Contact")
    print("5. Search Email")
    print("6. Update Contact")
    print("7. Delete Contact")
    print("8. Filter By Group")
    print("9. Sort Contacts")
    print("10. Add Phone")
    print("11. Move Contact To Group")
    print("12. Pagination")
    print("13. Export JSON")
    print("14. Import JSON")
    print("15. Exit")

    choice = input("Select Option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        import_csv()
    elif choice == "3":
        show_contacts()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        search_email()
    elif choice == "6":
        update_contact()
    elif choice == "7":
        delete_contact()
    elif choice == "8":
        filter_group()
    elif choice == "9":
        sort_contacts()
    elif choice == "10":
        add_phone()
    elif choice == "11":
        move_group()
    elif choice == "12":
        pagination()
    elif choice == "13":
        export_json()
    elif choice == "14":
        import_json()
    elif choice == "15":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
