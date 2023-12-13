-- update Bob's score to 10
--you're not allowed to use bob's id value, only name field
UPDATE `second_table`
SET `score` = 10
WHERE `score` =
(SELECT `score`
FROM `second_table`
WHERE `name` = 'Bob');
