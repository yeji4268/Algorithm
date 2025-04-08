-- 출럭: 아이템ID, 아이템 이름
-- 조건: root 아이템
-- 정렬: 아이템ID ASC
SELECT A.item_id, A.item_name
FROM item_info A, item_tree B
WHERE A.item_id = B.item_id
  and B.parent_item_id IS NULL
ORDER BY A.item_id; 