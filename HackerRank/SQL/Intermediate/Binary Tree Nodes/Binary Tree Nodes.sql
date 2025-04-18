SELECT n, CASE WHEN p IS NULL THEN 'Root'
               WHEN n NOT IN (SELECT DISTINCT p FROM bst WHERE p IS NOT NULL) THEN 'Leaf'
               ELSE 'Inner'
          END AS nodeType
FROM bst
ORDER BY n; 