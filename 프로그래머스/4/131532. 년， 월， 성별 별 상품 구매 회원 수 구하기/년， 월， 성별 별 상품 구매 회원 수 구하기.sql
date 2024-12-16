-- 코드를 입력하세요
SELECT EXTRACT(YEAR FROM SALES_DATE) YEAR,
    EXTRACT(MONTH FROM SALES_DATE) MONTH, 
        gender, 
        count(distinct b.user_id)
from user_info a, online_sale b
where a.user_id = b.user_id and gender is not null
group by EXTRACT(YEAR FROM SALES_DATE), EXTRACT(MONTH FROM SALES_DATE),  gender
order by EXTRACT(YEAR FROM SALES_DATE), EXTRACT(MONTH FROM SALES_DATE),  gender