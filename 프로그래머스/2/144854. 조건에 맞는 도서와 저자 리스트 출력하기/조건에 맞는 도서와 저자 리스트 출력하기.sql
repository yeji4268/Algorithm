-- 코드를 입력하세요
select a.book_id, author_name, to_char(published_date, 'YYYY-MM-DD')
from book a, author b
where a.author_id = b.author_id
    and category = '경제'
order by published_date ;