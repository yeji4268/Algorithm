-- 코드를 입력하세요
SELECT '/home/grep/src/'||a.board_id||'/'||file_id||file_name||file_ext as FILE_PATH
FROM USED_GOODS_BOARD A, USED_GOODS_FILE B
WHERE A.board_id = B.board_id
	and a.views in (select max(views)
    				from used_goods_board)
order by file_id desc