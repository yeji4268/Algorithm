SELECT CASE WHEN B.grade >= 8 THEN A.name 
            ELSE 'NULL'
       END as name, B.grade, A.marks
FROM students A
JOIN grades B
    ON A.marks BETWEEN B.min_mark AND B.max_mark
ORDER BY B.grade DESC, 
    CASE 
        WHEN B.grade >= 8 THEN A.Name
        ELSE NULL
    END ASC,
    CASE 
        WHEN B.grade < 8 THEN A.Marks
        ELSE NULL
    END ASC;