-- =========================
-- TSIS1 Extended PhoneBook
-- =========================

DROP TABLE IF EXISTS phones CASCADE;
DROP TABLE IF EXISTS contacts CASCADE;
DROP TABLE IF EXISTS groups CASCADE;

-- Groups table
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Contacts table
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100),
    birthday DATE,
    group_id INTEGER REFERENCES groups(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Phones table
CREATE TABLE phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(10)
        CHECK(type IN ('home','work','mobile'))
);

-- Default groups
INSERT INTO groups(name)
VALUES
('Family'),
('Friend'),
('Work'),
('Other')
ON CONFLICT(name) DO NOTHING;
