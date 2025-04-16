SELECT ROUND(lat_n, 4)
FROM (SELECT lat_n, PERCENT_RANK() OVER (ORDER BY lat_n) as percent
      FROM station) A
WHERE A.percent = 0.5; 