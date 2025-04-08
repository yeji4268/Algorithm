-- 출력: 물고기의 수(FISH_COUNT), 이름(FISH_NAME)
-- 조건: 1) 종류별 2)  정렬: FIST_COUNT DESC
select A.fish_count, B.fish_name
from (
    select fish_type, count(id) as fish_count
    from fish_info
    group by fish_type
) A
left join fish_name_info B
on A.fish_type = B.fish_type
order by fish_count desc ;