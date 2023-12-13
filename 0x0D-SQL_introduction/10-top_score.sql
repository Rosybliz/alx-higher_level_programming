-- script thaat lists all records of secondTable 
-- result should display both score and name in thaat order
-- record should be ordered by score top ffirst
SELECT `score`, `name`
FROM second_table
ORDER BY `score` DESC, `name`;
