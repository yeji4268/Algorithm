-- 코드를 입력하세요
select count(*) as users
from user_info
where to_char(joined, 'YYYY') = '2021'
    and age between 20 and 29;