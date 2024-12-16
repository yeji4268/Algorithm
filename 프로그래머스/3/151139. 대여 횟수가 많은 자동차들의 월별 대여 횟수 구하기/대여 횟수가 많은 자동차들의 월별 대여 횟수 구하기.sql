-- 코드를 입력하세요
select extract(month from start_date) as MONTH, car_id, count(history_id) as RECORDS
from car_rental_company_rental_history
where start_date between to_date('2022-08-01', 'YYYY-MM-DD') and to_date('2022-10-31', 'YYYY-MM-DD')
    and car_id in (select car_id 
                from car_rental_company_rental_history
                WHERE START_DATE BETWEEN to_date('2022-08-01', 'YYYY-MM-DD') and to_date('2022-10-31', 'YYYY-MM-DD')
                 group by car_id
                 having count(car_id) >= 5
                )
group by extract(month from start_date), car_id
having count(HISTORY_ID) > 0
order by extract(month from start_date), car_id desc;