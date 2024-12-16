-- 코드를 입력하세요
SELECT title, a.board_id, b.reply_id, b.writer_id, b.contents, 
to_char(b.created_date, 'YYYY-MM-DD')
from used_goods_board a, used_goods_reply b
where a.board_id = b.board_id
    and to_char(a.created_date, 'YYYYMM') = '202210'
order by b.created_date, a.title;