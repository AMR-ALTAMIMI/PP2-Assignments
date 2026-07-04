-- 1. Function that returns all records matching a pattern
CREATE OR REPLACE FUNCTION search_contacts(search_text VARCHAR)
RETURNS TABLE(
    id INTEGER,
    username VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.phone
    FROM phonebook p
    WHERE p.username ILIKE '%' || search_text || '%'
       OR p.phone ILIKE '%' || search_text || '%';
END;
$$ LANGUAGE plpgsql;

-- 4. Function that queries data from the table with pagination
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(
    id INTEGER,
    username VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
