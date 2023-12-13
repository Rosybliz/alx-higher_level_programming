-- lists all records with score >= 10 in second_table
-- display both score and name in this order
-- scores ordered bt top first
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC, `name`;
