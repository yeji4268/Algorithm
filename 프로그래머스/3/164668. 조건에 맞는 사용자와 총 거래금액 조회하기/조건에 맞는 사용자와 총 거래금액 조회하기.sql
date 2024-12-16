select user_id, nickname, total_price
from used_goods_user a
inner join (select writer_id, sum(price) as total_price
            from used_goods_board
            where status = 'DONE'
            group by writer_id
            having sum(price) >= 700000) b
on a.user_id = b.writer_id
order by total_price;