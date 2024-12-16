select flavor
from (select a.flavor, 
          sum(a.total_order), 
          sum(b.total_order), 
          sum(a.total_order + b.total_order) as tot
    from july a, first_half b
    where a.flavor = b.flavor
    group by a.flavor
    order by tot desc)
where rownum <= 3;