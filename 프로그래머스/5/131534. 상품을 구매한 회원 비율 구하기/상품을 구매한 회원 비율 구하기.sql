SELECT YEAR(A.sales_date) as year, MONTH(A.sales_date) as month,
       COUNT(DISTINCT B.user_id) AS purchase_users,
       ROUND(COUNT(DISTINCT B.user_id) / (SELECT COUNT(user_id) FROM user_info WHERE YEAR(joined) = 2021), 1) AS purchase_ratio
FROM online_sale A
LEFT JOIN user_info B
ON A.user_id = B.user_id
WHERE YEAR(B.joined) = 2021
GROUP BY YEAR(A.sales_date), MONTH(A.sales_date)
ORDER BY YEAR(A.sales_date), MONTH(A.sales_date); 
