CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    c_id INTEGER;
BEGIN
    SELECT id
    INTO c_id
    FROM contacts
    WHERE name = p_contact_name;

    IF c_id IS NULL THEN
        RAISE NOTICE 'Contact not found.';
        RETURN;
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES(c_id, p_phone, p_type);
END;
$$;
