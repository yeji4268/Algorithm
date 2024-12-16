select category, sum(sales) as TOTAL_SALES
from book a, book_sales b
where a.book_id = b.book_id 
    and to_char(sales_date, 'YYYYMM') = '202201'
group by category
order by category ;