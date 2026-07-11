-- ======================================
-- TSIS1 Functions
-- ======================================

-- Search by name, email or any phone number
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(
    id INT,
    username VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    phone_type VARCHAR,
    group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.username,
        c.email,
        p.phone,
        p.type,
        g.name
    FROM contacts c
    LEFT JOIN phones p
        ON c.id = p.contact_id
    LEFT JOIN groups g
        ON c.group_id = g.id
    WHERE
        c.username ILIKE '%' || p_query || '%'
        OR c.email ILIKE '%' || p_query || '%'
        OR p.phone ILIKE '%' || p_query || '%';
END;
$$;
