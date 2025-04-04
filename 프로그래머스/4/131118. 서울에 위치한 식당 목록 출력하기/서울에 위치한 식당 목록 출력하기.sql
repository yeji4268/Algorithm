SELECT A.rest_id, A.rest_name, A.food_type, A.favorites, A.address, B.score
FROM rest_info A,
     (SELECT rest_id, 
             ROUND(AVG(review_score), 2) AS score 
      FROM rest_review 
      GROUP BY rest_id) B
WHERE A.rest_id = B.rest_id
  AND A.address LIKE '서울%'
ORDER BY B.score DESC, A.favorites DESC;
