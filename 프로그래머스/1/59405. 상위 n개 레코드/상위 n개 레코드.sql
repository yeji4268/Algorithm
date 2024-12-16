SELECT *
  FROM (SELECT NAME
          FROM ANIMAL_INS
         order by DATETIME asc 
       )
WHERE rownum = 1