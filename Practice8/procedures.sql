-- 2. Procedure to insert a new user; if user already exists, update their phone
-- Matches uniqueness on username constraint
CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_username VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phonebook (username, phone)
    VALUES (p_username, p_phone)
    ON CONFLICT (username) 
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$;

-- 3. Procedure to bulk insert users, evaluate phone correctness inside a loop & IF statement, and return faulty data.
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    IN p_usernames VARCHAR[],
    IN p_phones VARCHAR[],
    OUT failed_usernames VARCHAR[],
    OUT failed_phones VARCHAR[]
) 
LANGUAGE plpgsql 
AS $$
DECLARE
    i INT;
    v_phone VARCHAR;
BEGIN
    -- Initialize empty arrays for bad data collection
    failed_usernames := '{}';
    failed_phones := '{}';
    
    FOR i IN 1..array_length(p_usernames, 1) LOOP
        v_phone := p_phones[i];
        
        -- Phone validation conditional (Matches digits only and standard length bounds)
        IF v_phone SIMILAR TO '[0-9]+' AND length(v_phone) >= 10 AND length(v_phone) <= 15 THEN
            INSERT INTO phonebook (username, phone) 
            VALUES (p_usernames[i], v_phone)
            ON CONFLICT (username) DO UPDATE SET phone = EXCLUDED.phone;
        ELSE
            -- Appends invalid datasets to our tracking arrays
            failed_usernames := array_append(failed_usernames, p_usernames[i]);
            failed_phones := array_append(failed_phones, v_phone);
        END IF;
    END LOOP;
END;
$$;

-- 5. Procedure to delete data from the table by username OR phone
CREATE OR REPLACE PROCEDURE delete_contact(p_identifier VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = p_identifier OR phone = p_identifier;
END;
$$;
