-- 코드를 입력하세요
SELECT to_char(sales_date, 'YYYY-MM-DD') as sales_date, product_id, user_id, sales_amount
from online_sale
where to_char(sales_date, 'YYYYMM') = '202203'
union all
select to_char(sales_date, 'YYYY-MM-DD') as sales_date, product_id, null as user_id, sales_amount
from offline_sale
where to_char(sales_date, 'YYYYMM') = '202203'
order by sales_date, product_id, user_id;