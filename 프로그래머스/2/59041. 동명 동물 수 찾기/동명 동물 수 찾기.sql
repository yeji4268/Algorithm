-- 코드를 입력하세요
select name, count(name) as count
from animal_ins
group by name
having count(name) > 1
order by name;