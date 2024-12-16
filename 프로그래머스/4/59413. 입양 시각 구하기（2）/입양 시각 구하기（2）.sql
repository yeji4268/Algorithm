with h as (select level-1 as hour
          from dual
          connect by level <= 24)
select hour, count(animal_id) as COUNT
from h h left outer join animal_outs b 
on h.hour = to_number(to_char(cast(b.datetime as date), 'HH24'))
group by hour
order by hour;