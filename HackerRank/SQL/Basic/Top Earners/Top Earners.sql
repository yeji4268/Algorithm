SELECT salary * months AS tot_earnings, COUNT(*)
FROM employee
GROUP BY tot_earnings
ORDER BY tot_earnings desc
LIMIT 1; 