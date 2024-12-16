select member_name, review_text, to_char(review_date, 'YYYY-MM-DD')
from member_profile a, rest_review b
where a.member_id = b.member_id
    and b.member_id in (select member_id
                    from (select member_id, count(*) as cnt
                         from rest_review
                         group by member_id
                         order by cnt desc)
                    where rownum <= 1)
order by review_date, review_text;