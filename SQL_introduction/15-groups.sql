-- Lists the number of record with the same score in the table
SELECT score, count(*) AS number 
FROM second_table
GROUP BY score
ORDER BY number DESC;
