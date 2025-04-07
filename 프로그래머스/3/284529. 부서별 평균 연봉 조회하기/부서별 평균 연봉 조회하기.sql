SELECT A.dept_id, A.dept_name_en, ROUND(AVG(B.sal)) AS avg_sal
FROM hr_department A, hr_employees B
WHERE A.dept_id = B.dept_id
GROUP BY A.dept_id
ORDER BY avg_sal DESC; 