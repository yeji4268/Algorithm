WITH avg_score AS (
    SELECT emp_no, AVG(score) AS avg_score
    FROM hr_grade
    GROUP BY emp_no
)
SELECT A.emp_no, A.emp_name,
        CASE WHEN B.avg_score >= 96 THEN 'S'
             WHEN B.avg_score >= 90 THEN 'A'
             WHEN B.avg_score >= 80 THEN 'B'
             ELSE 'C'
        END AS grade,
        CASE WHEN B.avg_score >= 96 THEN A.sal * 0.2
             WHEN B.avg_score >= 90 THEN A.sal * 0.15
             WHEN B.avg_score >= 80 THEN A.sal * 0.1
             ELSE 0
        END AS bonus
FROM hr_employees A, avg_score B
WHERE A.emp_no = B.emp_no
GROUP BY B.emp_no;