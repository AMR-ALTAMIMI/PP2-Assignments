import re

# Function to add a new contact
def add_contact(name, phone):

    # Regular Expression Pattern
    # ^        -> Start of the string
    # \+77     -> The phone number must start with +77
    # \d{9}    -> Followed by exactly 9 digits
    # $        -> End of the string
    pattern = r"^\+77\d{9}$"

    # Check if the phone number matches the required format
    if re.match(pattern, phone):

        # Connect to the PostgreSQL database
        conn = get_db_connection()

        # Create a cursor object
        cur = conn.cursor()

        # SQL query to insert the contact
        cur.execute(
            "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
            (name, phone)
        )

        # Save the changes
        conn.commit()

        # Close the cursor
        cur.close()

        # Close the database connection
        conn.close()

        print("Contact added successfully!")

    else:
        # If the phone number format is incorrect
        print("Error: Write the Number in correct format (e.g., +77123456789)")
