-- Task 1: 
-- Create a table, rename it, add a column,
-- insert rows, update and delete data.

-- 1. Create a table
CREATE TABLE animals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    age INTEGER
);

-- 2. Rename the table
ALTER TABLE animals RENAME TO pets;

-- 3. Add a new column
ALTER TABLE pets ADD COLUMN owner TEXT;

-- 4. Insert rows into the table
INSERT INTO pets (name, species, age, owner)
VALUES ('Rex', 'Dog', 5, 'Anna');

INSERT INTO pets (name, species, age, owner)
VALUES ('Misty', 'Cat', 3, 'Oleh');

-- 5. Update a row
UPDATE pets
SET age = 6
WHERE name = 'Rex';

-- 6. Delete a row
DELETE FROM pets
WHERE name = 'Misty';
