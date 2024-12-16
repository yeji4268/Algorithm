-- 코드를 입력하세요
select member_id, member_name, gender, to_char(date_of_birth, 'YYYY-MM-DD')
from member_profile
where to_char(date_of_birth, 'MM') = '03'
    and gender = 'W'
    and tlno is not null
order by member_id;