-- 출력: 점수, 사번, 성명, 직책, 이메일
-- 조건: 평가 점수의 합이 가장 높은 사원
SELECT SUM(B.score) AS score, A.emp_no, A.emp_name, A.position, A.email
FROM hr_employees A, hr_grade B
WHERE A.emp_no = B.emp_no
GROUP BY A.emp_no
ORDER BY SUM(B.score) DESC
LIMIT 1;