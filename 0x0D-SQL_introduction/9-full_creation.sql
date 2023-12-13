-- adds multiple rows to a second table
-- if table exists, the script should not fail
CREATE TABLE IF NOT EXISTS `second_table`
(`id` INT, `name` VARCHAR(256), `score` INT);

INSERT INTO second_table
VALUES
(1, 'John', 10), (2, 'Alex', 3),
(3, 'Bob', 14), (4, 'George', 8);
