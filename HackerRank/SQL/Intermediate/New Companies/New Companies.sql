SELECT A.company_code, A.founder, 
        COUNT(DISTINCT B.lead_manager_code),
        COUNT(DISTINCT C.senior_manager_code),
        COUNT(DISTINCT D.manager_code),
        COUNT(DISTINCT D.employee_code)
FROM company A, lead_manager B, senior_manager C, employee D
WHERE A.company_code = B.company_code
  AND A.company_code = C.company_code
  AND A.company_code = D.company_code
GROUP BY A.company_code, A.founder
ORDER BY A.company_code; 