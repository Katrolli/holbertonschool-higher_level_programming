-- showing score as numbers
SELECT score, COUNT(score) AS numbers FROM second_table GROUP BY score; 
