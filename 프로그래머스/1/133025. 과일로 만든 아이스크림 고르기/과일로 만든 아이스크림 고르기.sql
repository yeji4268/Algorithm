-- 코드를 입력하세요
select a.flavor
from first_half a, icecream_info b
where a.flavor = b.flavor
    and ingredient_type = 'fruit_based'
    and total_order >= 3000
order by total_order desc;