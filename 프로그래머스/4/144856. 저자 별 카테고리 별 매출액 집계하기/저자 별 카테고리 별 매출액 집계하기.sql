-- 코드를 입력하세요
select a.author_id, author_name, category, sum(price * SALES) as total_sales
from book a, author b, book_sales c
where a.author_id = b.author_id
    and a.book_id = c.book_id
    and to_char(sales_date, 'YYYYMM') = '202201'
group by a.author_id,b.author_name,  a.category
order by a.author_id,b.author_name,  a.category desc;