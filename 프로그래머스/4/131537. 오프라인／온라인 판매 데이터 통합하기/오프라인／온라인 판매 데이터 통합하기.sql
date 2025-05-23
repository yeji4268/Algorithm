-- 코드를 입력하세요
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') SALES_DATE, 
        PRODUCT_ID, 
        USER_ID, 
        SALES_AMOUNT
FROM ONLINE_SALE
WHERE date_format(sales_date, '%Y-%m') = '2022-03'

UNION ALL

SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') SALES_DATE,
        PRODUCT_ID, 
        NULL AS USER_ID,
        SALES_AMOUNT
FROM OFFLINE_SALE
WHERE date_format(sales_date, '%Y-%m') = '2022-03'

ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;