import psycopg2
import csv
from connect import connect


# Create PhoneBook table
def create_table():
    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook(
            id SERIAL PRIMARY KEY,
            username VARCHAR(50),
            phone VARCHAR(20)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


# Add contact manually
def add_contact():
    conn = connect()
    cur = conn.cursor()

    username = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO PhoneBook(username, phone) VALUES(%s,%s)",
        (username, phone)
    )

    conn.commit()

    print("Contact added successfully!")

    cur.close()
    conn.close()


# Import contacts from CSV
def import_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            cur.execute(
                "INSERT INTO PhoneBook(username, phone) VALUES(%s,%s)",
                (row[0], row[1])
            )

    conn.commit()

    print("Contacts imported successfully!")

    cur.close()
    conn.close()


# Show all contacts
def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM PhoneBook")

    rows = cur.fetchall()

    print("\n------ Contact List ------")

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Search contact
def search_contact():
    conn = connect()
    cur = conn.cursor()

    print("1. Search by Name")
    print("2. Search by Phone Prefix")

    choice = input("Choose: ")

    if choice == "1":

        name = input("Enter name: ")

        cur.execute(
            "SELECT * FROM PhoneBook WHERE username=%s",
            (name,)
        )

    elif choice == "2":

        prefix = input("Enter phone prefix: ")

        cur.execute(
            "SELECT * FROM PhoneBook WHERE phone LIKE %s",
            (prefix + "%",)
        )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Update contact
def update_contact():
    conn = connect()
    cur = conn.cursor()

    name = input("Enter current name: ")

    print("1. Update Name")
    print("2. Update Phone")

    choice = input("Choose: ")

    if choice == "1":

        new_name = input("New name: ")

        cur.execute(
            "UPDATE PhoneBook SET username=%s WHERE username=%s",
            (new_name, name)
        )

    elif choice == "2":

        new_phone = input("New phone: ")

        cur.execute(
            "UPDATE PhoneBook SET phone=%s WHERE username=%s",
            (new_phone, name)
        )

    conn.commit()

    print("Contact updated!")

    cur.close()
    conn.close()


# Delete contact
def delete_contact():
    conn = connect()
    cur = conn.cursor()

    print("1. Delete by Name")
    print("2. Delete by Phone")

    choice = input("Choose: ")

    if choice == "1":

        name = input("Enter name: ")

        cur.execute(
            "DELETE FROM PhoneBook WHERE username=%s",
            (name,)
        )

    elif choice == "2":

        phone = input("Enter phone: ")

        cur.execute(
            "DELETE FROM PhoneBook WHERE phone=%s",
            (phone,)
        )

    conn.commit()

    print("Contact deleted!")

    cur.close()
    conn.close()


# Main Menu
def menu():

    create_table()

    while True:

        print("\n========== PhoneBook ==========")
        print("1. Add Contact")
        print("2. Import Contacts from CSV")
        print("3. Show Contacts")
        print("4. Search Contact")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            import_csv()

        elif choice == "3":
            show_contacts()

        elif choice == "4":
            search_contact()

        elif choice == "5":
            update_contact()

        elif choice == "6":
            delete_contact()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
